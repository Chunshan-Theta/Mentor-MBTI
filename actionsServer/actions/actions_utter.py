# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# from .models import callGPT_AnswerQuestion
# from .db import getKN
import json
import os


def send(d: CollectingDispatcher, obj: Any): d.utter_message(str(obj))
def getSlot_Stage(t: Tracker): return t.get_slot('stage')
def getUserLatestMEG(t: Tracker): return t.latest_message
def getUserText(t: Tracker): return getUserLatestMEG(t)["text"]



class ActionUtterStoryStart(Action):
    def name(self) -> Text:
        return "action_story_start"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = """
        你遭遇了不幸的事故，雖然失去了生命，但幸運的是，這並不是旅程的終點。由於未知的原因，你發現自己被傳送到了另一個世界，一個充滿夢想、魔法和龍的國度。你已經到達了一個美麗而神秘的國度，稱為埃爾多利亞，充滿了奇幻的生物和魔法力量。
        你發現自己擁有一些特殊的能力，你會在這個平行世界中逐發現，同時你可以自由地探索不同的地方，遭遇冒險事件。
        現在你遇到了一位來自當地的魔法公主，她正面臨一個難題，需要你的幫助。
        她告訴你 ：親愛的旅行者，我是埃爾多利亞的公主妮娜。我們的國家正面臨一個嚴重的危機。在遠古的傳說中，有一個邪惡的巫師被封印在深淵之中，他擁有無窮的黑暗力量。然而，最近我們的封印之力開始變弱，巫師的黑暗力量即將被釋放出來。
        為了保護我們的國家和人民，我需要找到並重新封印巫師。但是，我不能單獨完成這個任務，我需要你的幫助。你願意幫助我嗎？
        
        選擇1：當然願意！我願意冒險去尋找並重新封印巫師。
        選擇2：我很抱歉，我不願意冒險，這太危險了。
        選擇3：我需要更多的信息才能做出決定。"
        """
        for m in text.split("\n"):
            dispatcher.utter_message(text=str(m))
        return []
