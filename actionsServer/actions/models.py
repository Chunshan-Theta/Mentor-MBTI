import requests
import json
from typing import List, Any, Dict
import os


def callGpt(
        userText: str,
        messages: List[Any],
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
        "max_tokens": 250,
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
While you already collected enough data could know the detailed personality of the user, you must actively terminate the discussion, and finish the story in one line with the pattern "<the ending of story> ***【故事结束】 ". 

FOLLOW ABOVE RULE.

"""

gptOpener: str ="""
Next, I will describe your background and the decision points you are facing. I will also provide three choices for you to make, or you can describe your own thoughts. 
"""

gptBackground: str ="""
你遭遇了不幸的事故，雖然失去了生命，但幸運的是，這並不是旅程的終點。由於未知的原因，你發現自己被傳送到了另一個世界，一個充滿夢想、魔法和龍的國度。你已經到達了一個美麗而神秘的國度，稱為埃爾多利亞，充滿了奇幻的生物和魔法力量。
你發現自己擁有一些特殊的能力，你會在這個平行世界中逐發現，同時你可以自由地探索不同的地方，遭遇冒險事件。
現在你遇到了一位來自當地的魔法公主，她正面臨一個難題，需要你的幫助。
她告訴你 ：
"""

gptDefaultStory: str ="""
"親愛的旅行者，我是埃爾多利亞的公主妮娜。我們的國家正面臨一個嚴重的危機。在遠古的傳說中，有一個邪惡的巫師被封印在深淵之中，他擁有無窮的黑暗力量。然而，最近我們的封印之力開始變弱，巫師的黑暗力量即將被釋放出來。為了保護我們的國家和人民，我需要找到並重新封印巫師。但是，我不能單獨完成這個任務，我需要你的幫助。你願意幫助我嗎？

選擇1：當然願意！我願意冒險去尋找並重新封印巫師。
選擇2：我很抱歉，我不願意冒險，這太危險了。
選擇3：我需要更多的信息才能做出決定。"
"""

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
def callGPT_ExtendStory(memory: List[Dict[str, str]],userText: str) -> (str, List[Dict[str,str]]):
        memory.extend([{"role": "user", "content": userText}])
        botReply: str =  callGpt(userText, memory,0.7)
        memory.extend([{"role": "assistant", "content": botReply}])
        return botReply, memory
        