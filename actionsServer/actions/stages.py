from typing import List, Dict, Any

class Stage:
    def __init__(self, _dict):
        # TODO: Check `_dict` is valid 
        self.__dict__.update(_dict)
    
    def __str__(self):
        return str(self.__dict__)



class Memory:
    def __init__(self, _dict=None):
        if _dict is not None:
            self.__dict__.update(_dict)
        else:
            self.__dict__.update({})

    def setMemory(self, key: str, obj: Any):
        self.__dict__[key] = obj
    
    def getMemory(self, key: str) -> Any | None:
        
        return self.__dict__[key] if key in self.__dict__ else None





       
mentaltutor_storiesGamer = Stage({
    "system": {
            'id': "mentaltutor_storiesGamer",
            'type': "interactive"
        },
    "situation": {
        'role': """
        You'll be playing the role of a counselor and having a conversation with a user to analyze their personality. This conversation will start by creating a made-up story together, with the user as the main character. Throughout this story-building process, the user will face different decision points, and they'll be asked to decide what happens next in the story.
        Once the story is finished, we'll analyze and estimate the user's personality based on how they made those decisions."""
    },
    "target": {
        'jobs': [
            "You need more than two questions to understand the user’s personality, so write new sections and questions for the user to collect more data. "
        ],
        'rules': [
            "While users already answer decision points encounter more than four decision points, you must actively terminate the discussion, and finish the story in one line",
            "While you already collected enough data could know the detailed personality of the user, you must actively terminate the discussion, and finish the story in one line",
            "When you finished the story, add the `[GAMEOVER]` label at the end.",
            "The entire conversation must be in Traditional Chinese."
        ],
    },
    "action": {
        'toAgent': [
            "Let's start the story now. Next, I will describe your background and the decision points you are facing. I will also provide three choices for you to make, or you can describe your own thoughts. "
        ],
        'both': [
            "你已經到達了一個美麗而神秘的國度，稱為埃爾多利亞，充滿了奇幻的生物和魔法力量。你發現自己擁有一些特殊的能力，你會在這個平行世界中逐發現，同時你可以自由地探索不同的地方，遭遇冒險事件。現在你遇到了一位來自當地的魔法公主，她告訴你 ：",
            "親愛的旅行者，我是埃爾多利亞的公主妮娜。我們的國家有一個邪惡的巫師被封印在深淵之中，他擁有無窮的黑暗力量。然而，最近我們的封印之力開始變弱，為了保護我們的國家和人民，我需要找到並重新封印巫師。",
            "但是，我不能單獨完成這個任務，我需要你的幫助。你願意幫助我嗎？\n選擇1：當然願意！我願意冒險去尋找並重新封印巫師。\n選擇2：我很抱歉，我不願意冒險，這太危險了。\n選擇3：我需要更多的信息才能做出決定。"
        ],
        'toUser': []
    },
    "response": {
        'storeFunc': [
            "mentaltutor-storiesgamer.history",
            "mentaltutor-storiesgamer.botReply",
            "mentaltutor-storiesgamer.simphistory",
            "mentaltutor-storiesgamer.decodeMemory",
        ],
        'toUserResponse': [
            "MEMORY:mentaltutor-storiesgamer.botReply"
        ],
        'agnetFinalPoint': [
            "keywork:[GAMEOVER]"
        ],
        'userFinalPoint': [
            "intent:ok"
        ],
        'nextStageId': "mentaltutor_mbtiScale",
    }
})

       
mentaltutor_mbtiScale = Stage({
    "system": {
            'id': "mentaltutor_mbtiScale",
            'type': "analysis"
        },
    "situation": {
        'role': """You'll be playing the role of a counselor and having a conversation with a user to analyze their personality. This conversation will start by creating a made-up story together, with the user as the main character. Throughout this story-building process, the user will face different decision points, and they'll be asked to decide what happens next in the story.
        Once the story is finished, we'll analyze and estimate the user's personality based on how they made those decisions."""
    },
    "target": {
        'jobs': [
            "Now that the story is finished, analyze and estimate the user's personality based on the story, the challenges faced, and the choices made"
        ],
        'rules': [
            "Please carefully review all the conversations provided by the user to analyze their personality. Based on the analysis, fill out the six-point MBTI questionnaire below for the user.",
            """six-point MBTI questionnaire ：
            --START--- 
            Personality Traits-> "<Description of User Personality Traits in traditional Mandarin in 50 words> “ 
            the Six-point mbti scale: 
            Extraversion (E)-> * of 6 
            Introversion (I)->* of 6 
            Sensing (S): * of 6 
            Intuition (N)->* of 6 
            Thinking (T)->* of 6 
            Feeling (F)->* of 6 
            Judging (J)-> * of 6 
            Perceiving (P)-> * of 6 
            MBTI-CODE -> <MBTI-CODE>""",
            "`Personality Traits` must be in Traditional Chinese."
        ],
    },
    "action": {
        'toAgent': [
            "以下為對話內容:",
            "MEMORY:mentaltutor-storiesgamer.simphistory"
        ],
        'both': [],
        'toUser': [
            "接下來要進行分析 請說`繼續`。"
        ]
    },
    "response": {
        'storeFunc': [
            "mentaltutor-storiesgamer.history",
            "mentaltutor-storiesgamer.botReply",
            "mentaltutor-mbtiscale.decodeAnalyzeStory",
        ],
        'toUserResponse': [
            "MEMORY:mentaltutor-mbtiscale.decodeAnalyzeStory"
        ],
        'agnetFinalPoint': [
            ""
        ],
        'userFinalPoint': [
            ""
        ],
        'nextStageId': "",
    }
})