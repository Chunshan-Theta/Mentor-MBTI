import requests
import json
from typing import List, Any, Dict
import os
from .document import *
from .stages import mentaltutor_storiesGamer, mentaltutor_mbtiScale

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

gptSystem: str = mentaltutor_storiesGamer.situation["role"]+"\n"+"\n".join(mentaltutor_storiesGamer.target["jobs"])+"\n"+"\n".join(mentaltutor_storiesGamer.target["rules"])

gptBackground: str = "\n".join(mentaltutor_storiesGamer.action["toAgent"])

gptDefaultStory: str ="\n".join(mentaltutor_storiesGamer.action["both"])
client = createClient()
assert(checkClient(client))

def initMemory(userText: str): return  [
                {
                    "role": "system",
                    "content": gptSystem
                },
                {
                    "role": "assistant",
                    "content": gptBackground+gptDefaultStory
                },
                {
                    "role": "user",
                    "content": userText
                }
        ]
def callGPT_ExtendStory(userId: str, userText: str) -> str:
    
    memory = getByKey(client, userId)
    if memory is None:
        memory = initMemory(userText)
    else:
        memory.extend([{"role": "user", "content": userText}])
    if len(memory) > 10:
        botReply: str =  callGpt(memory[:1]+memory[-10:], 0.7)
    else:
        botReply: str =  callGpt(memory, 0.7)


    memory.extend([{"role": "assistant", "content": botReply}])
    res = updateDocuments(client,[{
        'key': userId,
        'value': memory
    }],"$")
    assert(all(res))

    return botReply        

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
    
    memory = getByKey(client, userId)
    content: str = ""
    for m in memory[-10:]:
        if m["role"]=="assistant":
            subsentence = m["content"].split(" ")
            content+= m["role"]+": "+ "\n".join(subsentence[-5:])
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
                    "role": "assistant",
                    "content": content
                }
        ], 0.1)
    replies: List(str) = decodeAnalyzeStory(botReply)
    
    res = updateDocuments(client,[{
        'key': "replies~|~"+userId,
        'value': {"replies": replies}
    }],"$")
    assert(all(res))

    return botReply       