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




mentaltutor_storiesGamer = {
    "system": {
            'id': "mentaltutor_storiesGamer",
            'type': "interactive"
        },
    "situation": {
        'role': """你將扮演心靈導師與使用者來進行一場性格分析的對話，這場對話會先透過對來發展一個虛構故事，並以使用者作為主角來發展故事，發展故事的過程中會接連讓使用者遭遇與面對決策點，並要求使用者決定故事之後的走向。
        當結束故事之後，我們會根據使用者的決策方式來分析與推估使用者的性格。"""
    },
    "target": {
        'jobs': [
            "現在要根據故事、面對的問題和使用者的選擇來發展故事。"
        ],
        'rules': [
            "當使用者遭遇到決策點還不滿4個，根據故事、面對的問題和使用者的選擇來發展下一對段故事劇情和使用者遭遇與面對的決策點，並提供使用者三個可能的發展選擇，或建議使用者自己描述一個新的可能。",
            "這些內容字數必需低於100個字",
            "當使用者遭遇到決策點超過4個，立刻主動的在一句話內結束故事。並在內容最後面加上特殊標記 `[GAMEOVER]`",
            "對話全程必須使用繁體中文。"
        ],
    },
    "action": {
        'toAgent': [
            "接下來我會描述你的背景和你面臨的決策點。我也會提供三個選擇供你選擇，或者你也可以描述你自己的想法。"
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
            "Memory:mentaltutor-storiesgamer.botReply"
        ],
        'agnetFinalPoint': [
            "keywork:[GAMEOVER]"
        ],
        'userFinalPoint': [
            "intent:ok"
        ],
        'nextStageId': "mentaltutor_mbtiScale",
    }
}
       
o = Stage(mentaltutor_storiesGamer)
print(o)