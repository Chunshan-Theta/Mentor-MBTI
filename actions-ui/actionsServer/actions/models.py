import requests
import json
from typing import List, Any

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
        'Authorization': 'Bearer <GPT-KEY>'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return str(response.json()['choices'][0]['message']['content'])

def callGPT_finetuneQuestion(userText: str) -> str:
        return callGpt(userText, [
                {
                    "role": "system",
                    "content": """
                    我們是一個自然科的討論課程，你是這堂課的教師，你負責將學生的問題優化另一個問題，請理解學生的問題後提出更明確的問題。
                    切記我們不提出自然以外的內容，所有提出的問題維持在自然領域之中。
                    """
                },
                {"role": "user", "content": "蜘蛛 八隻腳"},
                {"role": "assistant", "content": "請問蜘蛛是八隻腳嗎"},
                {"role": "user", "content": userText}
        ],0.3)

def callGPT_AnswerQuestion(userText: str) -> str:
        return callGpt(userText, [
                {
                    "role": "system",
                    "content": """
                    我們是一個自然科的討論課程，你是這堂課的教師，你負責回應學生的問題，請理解學生的問題後提出明確的。
                    切記我們不提出自然以外的內容，所有提出的問題維持在自然領域之中。
                    """
                },
                {"role": "user", "content": "請問蜘蛛是八隻腳嗎"},
                {"role": "assistant", "content": "不是，大多數的蜘蛛是六隻腳"},
                {"role": "user", "content": userText}
        ],0.7)