import requests
import json
from typing import List, Any, Dict
import os
from .document import *
from .stages import mentaltutor_storiesGamer

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
        return "ERROR:"+str(response.text)


#
#
#
#

gptSystem: str = mentaltutor_storiesGamer.situation["role"]

gptOpener: str = "\n".join(mentaltutor_storiesGamer.target["jobs"])+"\n\n\n"+"\n".join(mentaltutor_storiesGamer.target["rules"])

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
                    "content": gptOpener+gptBackground+gptDefaultStory
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
    replies: List[str] = [] 
    replies.append("**botReply : "+botReply)   
    for m in botReply.split("\n"):
        if "->" in m :
            unit = m.split('->')
            keymap[unit[0].strip()] = unit[1].replace("of 6","").strip()
        elif ":" in m :
            unit = m.split(':')
            keymap[unit[0].strip()] = unit[1].replace("of 6","").strip()
    if "Personality Traits" in keymap:
        replies.append("您的性格 : "+keymap["Personality Traits"])
    if "MBTI-CODE" in keymap:
        replies.append("**MBTI-CODE : "+keymap["MBTI-CODE"]) 
        replies.append("更詳細可以參考MBTI官網: https://www.16personalities.com/"+keymap["MBTI-CODE"]+"-personality") 

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
                    "content": """
                    As a psychological counselor, your focus should be on analyzing the user's MBTI personality traits and providing corresponding explanations.
                    Please carefully review all the conversations provided by the user.
                    Please explain the reasons and fill in the six-point mbti scale for the user based on the following dialogue
                    """
                },
                {
                    "role": "user",
                    "content": """
                    
                    conversation:
                    """+ content + """

                    ---START---
                    Personality Traits-> "<Description of User Personality Traits in traditional Mandarin in 50 words>"

                    the Six-point mbti scale:
                    Extraversion (E)-> * of 6
                    Introversion (I)->*  of 6
                    Sensing (S): *  of 6
                    Intuition (N)->*  of 6
                    Thinking (T)->*  of 6
                    Feeling (F)->*  of 6
                    Judging (J)-> *  of 6
                    Perceiving (P)-> *  of 6

                    MBTI-CODE -> <MBTI-CODE>
                    ---FINISH--- 
                    the * is <score> you need to fill.


                    When answering, be sure not to include redundant premises, prefaces, warnings, suggestions and adjustments to the format, and fill it in exactly according to the format.
                    """
                }
        ], 0.3)
    replies: List(str) = decodeAnalyzeStory(botReply)
    
    res = updateDocuments(client,[{
        'key': "replies~|~"+userId,
        'value': {"replies": replies}
    }],"$")
    assert(all(res))

    return botReply       