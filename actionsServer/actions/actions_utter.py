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
import json
import os
from .stages import *


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

        stageObj: Stage = mentaltutor_storiesGamer
        for m in [
            "請詳讀以下情況，並根據自身情況思考後回應問題。",
            "您可以選擇提供您的選項，或是直接輸入你的想法"
        ]:
            dispatcher.utter_message(text=str(m))

        for m in stageObj.action["both"]:
            dispatcher.utter_message(text=str(m))

        return []
