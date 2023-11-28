import requests
import json
from typing import List, Any, Dict
import os
from .document import *
from .stages import *

def callGpt(
        messages: List[Dict[str,str]],
        temperature: float = 0.3
    ) -> str:
    url: str = "https://api.openai.com/v1/chat/completions"
    payload = json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": messages,
        "temperature": temperature,
        "top_p": 1,
        "n": 1,
        "stream": False,
        "max_tokens": 800,
        "presence_penalty": 0,
        "frequency_penalty": 0
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer '+ os.environ.get("ChatGPTApiKey", "None")
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    try:
        return str(response.json()['choices'][0]['message']['content'])
    except:
        return "OPEN API DOWN -> ERROR:"+str(response.text)


#
#
#
#


client = createClient()
assert(checkClient(client))


def decodeAnalyzeStory(botReply: str) -> List[str]:
    keymap = {}
    replies: List[str] = ["進行分析..."] 
    
    for m in botReply.split("^"):
        if "->" in m :
            unit = m.split('->')
            keymap[unit[0].strip()] = unit[1].replace("\n"," ").replace("of 6","").strip()
        elif ":" in m :
            unit = m.split(':')
            keymap[unit[0].strip()] = unit[1].replace("\n"," ").replace("of 6","").strip()
    if "Personality Traits" in keymap:
        replies.append("您的性格 : "+keymap["Personality Traits"])
    if "MBTI-CODE" in keymap:
        replies.append("更詳細可以參考MBTI官網: https://www.16personalities.com/"+keymap["MBTI-CODE"]+"-personality") 
        # replies.append("**MBTI-CODE : "+keymap["MBTI-CODE"]) 

    replies.append("**botReply : "+botReply)   
    replies.append("**keymap : "+json.dumps(keymap,ensure_ascii=False))      
    return replies

def callGPT_AnalyzeStory(userId: str) -> str:
    
    memory = getByKey(client, genKey(userId, "mentaltutor_storiesGamer", memoryLabels.stage["common"]["history"]))
    content: str = ""
    for m in memory[-10:]:
        if m["role"]=="assistant":
            subsentence = m["content"].split(" ")
            content+= m["role"]+": "+ "\n".join(subsentence[-8:])
            content+= "\n"
        else:
            content+= m["role"]+": "+ m["content"]
            content+= "\n"

    botReply: str = callGpt([
                {
                    "role": "system",
                    "content": mentaltutor_mbtiScale.situation["role"]+"\n"+"\n".join(mentaltutor_mbtiScale.target["jobs"])+"\n"+"\n".join(mentaltutor_mbtiScale.target["rules"])
                },
                {
                    "role": "assistant",
                    "content": "\n".join(mentaltutor_mbtiScale.action["toAgent"])+"\n".join(mentaltutor_mbtiScale.action["both"])
                },
                {
                    "role": "user",
                    "content": content
                }
        ], 0.01)
    replies: List(str) = decodeAnalyzeStory(botReply)
    
    res = updateDocuments(client,[{
        'key': "replies~|~"+userId,
        'value': {"replies": replies}
    }],"$")
    assert(all(res))

    return botReply       



#
#
#
def genKey(userId: str, stageId: str, actionLabel: str):
    return userId+"."+stageId+"."+actionLabel

def getLatestMemory(userId:str, stageObj: Stage ) -> List[Any] | None:
    memory = getByKey(client,genKey(userId, stageObj.system["id"], memoryLabels.stage["common"]["history"]))
    if memory is None:
        return None
    if len(memory) > 10:
        return memory[:1]+memory[-10:]
    else:
        return memory

def execStoreFunc(userId:str, stageObj: Stage, memory: List[Any], storeFunc: str, botReply: str) -> bool:
    if storeFunc == memoryLabels.stage["common"]["history"]:
        res = updateDocuments(client,[{
            'key': genKey(userId, stageObj.system["id"],memoryLabels.stage["common"]["history"]),
            'value': memory
        }],"$")
    elif storeFunc == memoryLabels.stage["common"]["botReply"]:
        res = updateDocuments(client,[{
            'key': genKey(userId, stageObj.system["id"], memoryLabels.stage["common"]["botReply"]),
            'value': botReply
        }],"$")
    elif storeFunc == memoryLabels.stage["common"]["simphistory"]:
        content: str = ""
        for m in memory[-10:]:
            if m["role"]=="assistant":
                subsentence = m["content"].split(" ")
                content+= m["role"]+": "+ "\n".join(subsentence[-5:])
                content+= "\n"
            else:
                content+= m["role"]+": "+ m["content"]
                content+= "\n"
        res = updateDocuments(client,[{
            'key': genKey(userId, stageObj.system["id"], memoryLabels.stage["common"]["simphistory"]),
            'value': content
        }],"$")
    else:
        raise Exception("Not Support storeFunc: "+storeFunc)
    return all(res)

def callGPTExecturer(userId: str, stageName: str, userText: str) -> str:
    
    # get Stage
    #   getStage(stageName: str) -> Stage
    if stageName == "mentalTutorStoriesGamer":
        stageObj: Stage = stageMap.mentalTutorStoriesGamer
    else:
        raise Exception("Not Support Stage")

    # get Stage type
    #   getStageType(stage: Stage) -> str(system-type)
    stageMode: String = stageObj.system["type"]

    # get Memory
    #   getMemory(userId: str, stageId: str, memoryLabel: str) -> Dict[str, Any]
    memory: List[Any] | None = getLatestMemory(userId, stageObj)


    botReply: str = "Bot Not Reply"
    if stageMode == "interactive":
        
        # build prompty
        #   buildPrompt(userId: str, stage: Stage) -> Dict[str, Any]
        if memory is None:
            memory: List[str] = [
                    {
                        "role": "system",
                        "content": stageObj.situation["role"]+"\n"+"\n".join(stageObj.target["jobs"])+"\n"+"\n".join(stageObj.target["rules"])
                    },
                    {
                        "role": "assistant",
                        "content": "\n".join(stageObj.action["toAgent"])+"\n".join(stageObj.action["both"])
                    },
                    {
                        "role": "user",
                        "content": userText
                    }
            ]
        else:
            memory.extend([{
                "role": "user",
                "content": userText
            }])

        # ask to bot
        botReply =  callGpt(memory, 0.7)
    else:
        raise Exception("Not Support stageMode Methods")
    memory.extend([{"role": "assistant", "content": botReply}])
    
    # Update memory
    #    getMemory(userId: str, stageId: str, memoryLabel: str, memory: Dict[str, Any]) -> bool
    for storeFunc in stageObj.response["storeFunc"]:
        assert(execStoreFunc(userId, stageObj, memory, storeFunc, botReply), "Failed stage: "+storeFunc)

    # answer to User
    #    buildReply(stage: Stage) -> str(botReply)
    return getByKey(client, genKey(userId,stageObj.system["id"], memoryLabels.stage["common"]["botReply"]))     