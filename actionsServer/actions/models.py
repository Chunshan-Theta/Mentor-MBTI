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


client = createClient()
assert(checkClient(client))

def setGameHistory(userId:str, memory: List[Any]):
    return updateDocuments(client,[{
            'key': userId+memoryTags.historyOfGame,
            'value': memory
        }],"$")
def getGameHistory(userId:str): return getByKey(client, userId + memoryTags.historyOfGame)
def setGameBotReply(userId:str, botReply: str):
    return updateDocuments(client,[{
            'key': userId+memoryTags.botReplyOfGame,
            'value': botReply
        }],"$")
def getGameBotReply(userId:str): return getByKey(client, userId + memoryTags.botReplyOfGame)
def setGameSimphistory(userId:str, memory: List[Any]):
    simphistory: str = ""
    for m in memory[-10:]:
        if m["role"]=="assistant":
            subsentence = m["content"].split(" ")
            simphistory+= m["role"]+": "+ "\n".join(subsentence[-5:])
            simphistory+= "\n"
        else:
            simphistory+= m["role"]+": "+ m["content"]
            simphistory+= "\n"
    return updateDocuments(client,[{
            'key': userId+memoryTags.simphistoryOfGame,
            'value': simphistory
        }],"$")
def getGameSimphistory(userId:str): return getByKey(client, userId + memoryTags.simphistoryOfGame)

def getLatestMemory(userId:str, stageObj: Stage ) -> List[Any] | None:
    memory = getGameHistory(userId)
    if memory is None:
        return None
    if len(memory) > 10:
        return memory[:1]+memory[-10:]
    else:
        return memory
#
#
#
#




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

    # replies.append("**botReply : "+botReply)   
    # replies.append("**keymap : "+json.dumps(keymap,ensure_ascii=False))
    replies.append("分析結束")            
    return replies

def callGPT_AnalyzeStory(userId: str) -> str:
    botReply: str = callGpt([
                {
                    "role": "system",
                    "content": mentaltutor_mbtiScale.situation["role"]+"\n"+"\n".join(mentaltutor_mbtiScale.target["jobs"])
                },
                {
                    "role": "assistant",
                    "content": "\n".join(mentaltutor_mbtiScale.action["toAgent"])
                },
                {
                    "role": "assistant",
                    "content": getGameSimphistory(userId)
                },
                {
                    "role": "assistant",
                    "content": "\n".join(mentaltutor_mbtiScale.target["rules"])
                }
        ], 0.01)
    replies: List(str) = decodeAnalyzeStory(botReply)
    

    return botReply       






#
#
#
def callGPTStoryExtend(userId: str, userText: str) -> str:
    
    # get Stage
    stageObj: Stage = mentaltutor_storiesGamer

    # get Memory
    memory: List[Any] | None = getLatestMemory(userId, stageObj)
        
    # build prompty
    if memory is None:
        memory: List[str] = [
                {
                    "role": "system",
                    "content": stageObj.situation["role"]+"\n"+"\n".join(stageObj.target["jobs"])+"\n"+"\n".join(stageObj.target["rules"])
                },
                {
                    "role": "assistant",
                    "content": "\n".join(stageObj.action["toAgent"])+"\n".join(stageObj.action["both"])
                },]
    memory.extend([{
        "role": "user",
        "content": userText
    }])

    # ask to bot
    botReply =  callGpt(memory, 0.7)
    memory.extend([{"role": "assistant", "content": botReply}])
    
    # Update memory
    _ = setGameHistory(userId, memory)
    _ = setGameBotReply(userId, botReply)
    _ + setGameSimphistory(userId, memory)
   

    return getGameBotReply(userId), len(getGameHistory(userId))+2   