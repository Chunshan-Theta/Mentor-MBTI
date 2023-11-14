import requests
import json
from typing import List, Any, Dict
import os
from .document import *

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

gptSystem: str = """
As a story-driven mental consultant, you need to understand the user's type through interactive conversation, you should continue the story and write more and new sections for the user to face difficult decisions. 
you need to continue the story and design the next section based on the user's decision.

Note that we must ONLY discuss the story and decision in traditional Mandarin, DO NOT  discuss anything else, like the MBTI framework!
You need more than two questions to understand the user’s personality, so write new sections and questions for the user to collect more data. 
But the count of sections CAN'T over 4.
While you already collected enough data could know the detailed personality of the user, you must actively terminate the discussion, and finish the story in one line with the pattern "<the ending of story> ***【GAMEOVER】 ". 
The Each Response JUST one line. 

FOLLOW ABOVE RULE.

"""

gptOpener: str ="""
Next, I will describe your background and the decision points you are facing. I will also provide three choices for you to make, or you can describe your own thoughts. 
"""

gptBackground: str ="""
你已經到達了一個美麗而神秘的國度，稱為埃爾多利亞，充滿了奇幻的生物和魔法力量。
你發現自己擁有一些特殊的能力，你會在這個平行世界中逐發現，同時你可以自由地探索不同的地方，遭遇冒險事件。
現在你遇到了一位來自當地的魔法公主，她告訴你 ：
"""

gptDefaultStory: str ="""
親愛的旅行者，我是埃爾多利亞的公主妮娜。我們的國家有一個邪惡的巫師被封印在深淵之中，他擁有無窮的黑暗力量。
然而，最近我們的封印之力開始變弱，為了保護我們的國家和人民，我需要找到並重新封印巫師。
但是，我不能單獨完成這個任務，我需要你的幫助。你願意幫助我嗎？

選擇1：當然願意！我願意冒險去尋找並重新封印巫師。
選擇2：我很抱歉，我不願意冒險，這太危險了。
選擇3：我需要更多的信息才能做出決定。"
"""
client = createClient()
assert(checkClient(client))

def initMemory(userText: str): return  [
                {
                    "role": "system",
                    "content": gptSystem
                },
                {
                    "role": "assistant",
                    "content": gptOpener+gptBackground
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
    # botReply: ---START--- Personality Traits-> "根據對話內容，用戶展現出了冒險、勇氣和決心的特質。他願意面對挑戰並克服困難，展現了冒險家的精神。"
    # the Six-point mbti scale: Extraversion (E)-> 3 of 6 Introversion (I)-> 3 of 6 Sensing (S): 3 of 6 Intuition (N)-> 3 of 6 Thinking (T)-> 2 of 6 Feeling (F)-> 4 of 6 Judging (J)-> 2 of 6 Perceiving (P)-> 4 of 6
    # MBTI-CODE -> INFP ---FINISH---
    
    # res = updateDocuments(client,[{
    #     'key': userId,
    #     'value': botReply
    # }],"$MBTIREPORT")
    # assert(all(res))

    return botReply       