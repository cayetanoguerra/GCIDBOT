from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import re


class ActionGetName(Action):

    def name(self) -> Text:
        return "action_get_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.latest_message['text'].split()[0]
        dispatcher.utter_message(text="Hola, " + name + ".")

        print(tracker.latest_message['text'])
        print(tracker.sender_id)

        return []


class ActionGetPhone(Action):

    def name(self) -> Text:
        return "action_get_phone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = tracker.latest_message['text']
        pattern = re.compile('(\+34|0034|34)?[ -]*([0-9])[ -]*([0-9][ -]*){8}')
        tlf = pattern.search(message).group()

        dispatcher.utter_message(text=tlf)

        print(tracker.latest_message['text'])
        print(tracker.sender_id)

        return []


class ActionDateConfirmation(Action):

    def name(self) -> Text:
        return "action_date_confirmation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Muy bien, ya tiene confirmada la fecha y hora de la prueba.")

        print(tracker.latest_message['text'])
        print(tracker.sender_id)

        return []


