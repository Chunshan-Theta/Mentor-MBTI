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
from .models import gptDefaultStory
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

        
        for m in gptDefaultStory.split("\n"):
            dispatcher.utter_message(text=str(m))
        return []
