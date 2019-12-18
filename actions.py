# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
# import question_queue
# import weather_api
from rasa_core_sdk import Action

logger = logging.getLogger(__name__)

# basic_info_flag = False

class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(
            requests.get("https://api.chucknorris.io/jokes/random").text
        )  # make an api call
        joke = request["value"]  # extract a joke from returned json response
        dispatcher.utter_message(joke)  # send the message back to the user
        return []


class ProvideWeather(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "get_weather"

    def run(self, dispatcher, tracker, domain):
        # what your action should do

        api_key = "60226e96c08099f9a5c196d66d4be818"
        api_url = "http://api.openweathermap.org/data/2.5/weather"

        zipcode_slot = tracker.get_slot('zipcode')
        query_string_payload = {'units': 'metric',
                                'zip': zipcode_slot, 'appid': api_key}

        response = requests.get(api_url, params=query_string_payload)

        response_data = response.json()

        temp_temp = int(response_data['main']['temp'])

        weather = str(temp_temp)
        # return nice text to the user
        weather_nice_text = "The temperature in " + tracker.get_slot('zipcode') + " is " + weather + " degrees Celsius"
        # send the message back to the user
        dispatcher.utter_message(weather_nice_text)
        return []

# prove I can add a random aspect to next question
# prove I can access the open slots logically


class CheckOpenSlots(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "get_open_slots"

    def run(self, dispatcher, tracker, domain):
        # what your action should do

        get_open_slots = tracker.current_slot_values()

        somestring = str(get_open_slots)

        # events can be used to set actions to take place in future

        # send the message back to the user
        dispatcher.utter_message(somestring)
        return []


# intial questions should quickly verify sets of information that are needed or not 


class DetermineNextQuestion(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "get_next_question"

    def run(self, dispatcher, tracker, domain):
        # what your action should do

        # for i in question queue that is also in slots filled, skip, else, ask question

        if tracker.get_slot('name') == None:
            # do something
            next_question = "Would you mind repeating your name?"
            dispatcher.utter_message(next_question)
            return
        elif tracker.get_slot('address') == None:
            # do something
            next_question = "Would you mind repeating your address?"
            dispatcher.utter_message(next_question)
            return
        elif tracker.get_slot('zipcode') == None:
            # do something
            next_question = "Would you mind repeating your zipcode?"
            dispatcher.utter_message(next_question)
            return
        elif tracker.get_slot('city') == None:
            # do something
            next_question = "Would you mind repeating your city?"
            dispatcher.utter_message(next_question)
            return
        elif tracker.get_slot('state') == None:
            # do something
            next_question = "Would you mind repeating your state?"
            dispatcher.utter_message(next_question)
            return
        exit_message = "basic information complete"
        dispatcher.utter_message(exit_message)
        return