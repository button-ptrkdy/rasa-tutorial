from json.decoder import JSONDecodeError
import subprocess

from typing import Any, Text, Dict, List
from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.events import EventType, SlotSet, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

import requests

class ActionPugme(Action):
def actionResetSlots(name, slots):
    """
    Generate an Action class to clear out defined slots.
    
    @param Text: name, Name of the action to generate.
    @param List[Text]: slots, List of slots to reset
    
    @return class: ActionResetSlots class
    """
    class ActionResetSlots(Action):
        def name(self) -> Text:
            return name

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            return [SlotSet(x, None) for x in slots]
    return ActionResetSlots

ActionResetDeploy = actionResetSlots('action_reset_deploy', ['application', 'version', 'environment', 'confirmation'])

class ActionResetSlots(Action):
    def name(self) -> Text:
        return "action_pugme"
        return 'action_reset_slots'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        r = requests.get('http://pugme.herokuapp.com/random')
        return [AllSlotsReset()]

        return [SlotSet('pug', r.json()['pug'])]
class FormActionDeploy(FormAction):
    """
    A FormAction to collect details about a requested deployment.
    """
    def name(self) -> Text:
        return "deploy_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["application", "version", "environment", "confirmation"]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        # utter submit template
        dispatcher.utter_message(template="utter_deploying")
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "application": [
                self.from_entity(entity="application"),
                self.from_text()
            ],
            "version": [
                self.from_entity(entity="version"),
                self.from_text()
            ],
            "environment" : [
                self.from_entity(entity="environment"),
                self.from_text()
            ],
            "confirmation" : [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False)
            ]
        }

class ActionHelloWorld(Action):
class ActionPugme(Action):
    """
    Simple action to display a random pug.
    """
    def name(self) -> Text:
        return "action_hello_world"
        return "action_pugme"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        r = requests.get('http://pugme.herokuapp.com/random')

        dispatcher.utter_message(text="Hello World!")

        return []
        return [SlotSet('pug', r.json()['pug'])]

class ActionButtonCli(Action):
    def name(self) -> Text:
        return "action_button_cli"

    """
    Action class for interacting with the Button CLI
    """
    def get_org_events(self, message, data):
        """
        Extract fields from an `org` type and return as slots.
        
        @param Text: message, Any header text sent before JSON
        @param Dict[Text, Any]: data, JSON object returned by server
        
        @return List[EventType]: List of slots to set and other events.
        """
        data.pop('id')
        data.pop('name')

@@ -75,32 +146,41 @@ def get_org_events(self, message, data):
            SlotSet('lookup_data', json.dumps(data))
        ]

    def name(self) -> Text:
        return "action_button_cli"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        thing = tracker.get_slot('lookup_thing')
        # pre-validated by the regex:lookup_thing entry in nlu.md
        kind, ident = thing.split('-', 1)
        events = []
        try:
            # Run the CLI container setup by docker-compose.override.yml
            # TODO: In production, this will need to change.
            result = subprocess.run(['docker', 'run', '-e', 'USER=docker',
                                     'rasa-demo_cli', 'get', thing],
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, 
                                    check=True)
            output = result.stdout.decode('utf8')
            # Button CLI output often begins with some log lines before JSON
            # NOTE: we assume that the first { indicates the beginning of the JSON
            json_start = output.index('{')
            message, src = output[:json_start], output[json_start:]
            data = json.loads(src)
            # If a 404 is raised...
            if(data.get('detail') == 'Not found.'):
                result = False
            # If a 500 is raised...
            elif('traceback' in data):
                result = False
                message += data.get('detail', '')
            else:
                result = True
                f = getattr(self, f'get_{kind}_events', None)
                events = f(message, data) if f else events

        except subprocess.CalledProcessError as e:
            message = "Error in CLI: " + e.stdout.decode('utf8')
            data = {}