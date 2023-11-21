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
from .models import callGPT_ExtendStory, callGPT_AnalyzeStory, decodeAnalyzeStory
import json
import os
from .document import *

def send(d: CollectingDispatcher, obj: Any): d.utter_message(str(obj))
def getSlot_StoryStage(t: Tracker): return t.get_slot('story_stage')
def getUserLatestMEG(t: Tracker): return t.latest_message
def getUserText(t: Tracker): return getUserLatestMEG(t)["text"]
def getUserId(t: Tracker): return t.sender_id
client = createClient()
assert(checkClient(client))


class ActionAskGptAnalysisStory(Action):

    def name(self) -> Text:
        return "action_ask_gpt_analysis_story"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        keymap = {}
        userText: str = getUserText(tracker)
        for reply in decodeAnalyzeStory(callGPT_AnalyzeStory(getUserId(tracker))):
            dispatcher.utter_message(text=reply) 
            
        return []


class ActionAskGptExtendStory(Action):
    def name(self) -> Text:
        return "action_ask_gpt_extend_story"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # dispatcher.utter_message(text="**CALL CUSTOM ACTION `action_ask_gpt_extend_story`")
        # dispatcher.utter_message(text="**user_text: `" + getUserText(tracker)+"`")
        # dispatcher.utter_message(text="**user sender_id: `"+tracker.sender_id+"`")
        botReply:str = callGPT_ExtendStory(getUserId(tracker), "我選擇是:"+getUserText(tracker))
        for m in botReply.split("\n"):
            dispatcher.utter_message(text=str(m))

        if "GAMEOVER" in botReply or "遊戲結束" in botReply:

            dispatcher.utter_message(text="遊戲將要結束 進行分析 沒問題請說繼續")
            return [
                SlotSet("story_started", False),
                SlotSet("story_finished", True)
            ]
        else:
            return []
