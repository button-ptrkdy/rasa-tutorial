## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_name <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 
## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks
 
## story_name
* name{"name":"Sam"}
 - utter_greet

## story_joke_01
* joke
 - action_joke

## story_joke_02
* greet
 - utter_name
* name{"name":"Lucy"} <!--- User response with an entity. In this case it represents user message 'My name is Lucy.' --> 
 - utter_greet
* joke
 - action_joke
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye 


 <!--- New Stories related to simple bot -->

## story_address
* provide_address
 - utter_address
 - get_next_question

## story_city
* provide_city
 - utter_city
 - get_next_question

## story_zipcode
* provide_zipcode
 - utter_zipcode
 - get_next_question

## story_state
* provide_state
 - utter_state
 - get_next_question

## story_weather
* weather
 - get_weather
 - get_next_question

## story_status
* status
 - get_open_slots
 - utter_status
 - get_next_question