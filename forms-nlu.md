## deploy application
* deploy+say_application
  - deploy_form
  - form{"name": "deploy_form"}
* affirm
  - form{"name": null}
  - utter_deploying
  - action_reset_slots

## deploy application [sad path]
* deploy+say_application
  - deploy_form
  - form{"name": "deploy_form"}
* deny
  - form{"name": null}
  - utter_cancelled
  - action_reset_slots

## deploy application to environment
* deploy+say_application+say_environment
  - deploy_form
  - form{"name": "deploy_form"}
* affirm
  - form{"name": null}
  - utter_deploying
  - action_reset_slots

## deploy application to environment [sad path]
* deploy+say_application+say_environment
  - deploy_form
  - form{"name": "deploy_form"}
* deny
  - form{"name": null}
  - utter_cancelled
  - action_reset_slots

## deploy application version to environment
* deploy+say_application+say_version+say_environment
  - deploy_form
  - form{"name": "deploy_form"}
* affirm
  - form{"name": null}
  - utter_deploying
  - action_reset_slots

## deploy application version to environment [sad path]
* deploy+say_application+say_version+say_environment
  - deploy_form
  - form{"name": "deploy_form"}
* deny
  - form{"name": null}
  - utter_cancelled
  - action_reset_slots

## frink
* frink
  - utter_would_frink

## pugme
* pugme
  - action_pugme
  - utter_pugme

## button cli happy
## button cli
* lookup
  - utter_looking
  - action_button_cli
  - slot{"lookup_result": true}
  - utter_lookup_success

## button cli sad
## button cli [sad path]
* lookup
  - utter_looking
  - action_button_cli
@@ -22,7 +80,6 @@
  - utter_greet
* mood_great{"mood": "good"}
  - utter_happy
  - action_hello_world

## sad path 1
* greet