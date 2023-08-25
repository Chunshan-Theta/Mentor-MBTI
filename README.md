# rasa

## Init a Project
```
# docker run --rm -it -v "./[PROJECT NAME]:/app" --name [PROJECT NAME] rasa/rasa:3.6.6-full init

docker run --rm -it -v "./newsletter:/app" --name rasa rasa/rasa:3.6.6-full init
```

```terminal
Welcome to Rasa! 🤖

To get started quickly, an initial project will be created.
If you need some help, check out the documentation at https://rasa.com/docs/rasa.
Now let's start! 👇🏽

? Please enter a path where the project will be created [default: current directory]
? Directory '/app' is not empty. Continue? Yes
2023-08-25 16:26:29 INFO     root  - copying /opt/venv/lib/python3.10/site-packages/rasa/cli/initial_project/domain.yml -> .
2023-08-25 16:26:29 INFO     root  - creating tests
2023-08-25 16:26:29 INFO     root  - copying /opt/venv/lib/python3.10/site-packages/rasa/cli/initial_project/tests/test_stories.yml -> ./tests
2023-08-25 16:26:29 INFO     root  - copying /opt/venv/lib/python3.10/site-packages/rasa/cli/initial_project/credentials.yml -> .
2023-08-25 16:26:29 INFO     root  - creating data
2023-08-25 16:26:29 INFO     root  - copying /opt/venv/lib/python3.10/site-packages/rasa/cli/initial_project/data/rules.yml -> ./data
2023-08-25 16:26:29 INFO     root  - copying /opt/venv/lib/python3.10/site-packages/rasa/cli/initial_project/data/nlu.yml -> ./data
2023-08-25 16:26:29 INFO     root  - copying /opt/venv/lib/python3.10/site-packages/rasa/cli/initial_project/data/stories.yml -> ./data
2023-08-25 16:26:29 INFO     root  - copying /opt/venv/lib/python3.10/site-packages/rasa/cli/initial_project/config.yml -> .
2023-08-25 16:26:29 INFO     root  - copying /opt/venv/lib/python3.10/site-packages/rasa/cli/initial_project/endpoints.yml -> .
2023-08-25 16:26:29 INFO     root  - creating actions
2023-08-25 16:26:29 INFO     root  - copying /opt/venv/lib/python3.10/site-packages/rasa/cli/initial_project/actions/actions.py -> ./actions
2023-08-25 16:26:29 INFO     root  - creating actions/__pycache__
2023-08-25 16:26:29 INFO     root  - copying /opt/venv/lib/python3.10/site-packages/rasa/cli/initial_project/actions/__pycache__/actions.cpython-310.pyc -> ./actions/__pycache__
2023-08-25 16:26:29 INFO     root  - copying /opt/venv/lib/python3.10/site-packages/rasa/cli/initial_project/actions/__pycache__/__init__.cpython-310.pyc -> ./actions/__pycache__
2023-08-25 16:26:29 INFO     root  - copying /opt/venv/lib/python3.10/site-packages/rasa/cli/initial_project/actions/__init__.py -> ./actions
Created project directory at '/app'.
Finished creating project structure.
? Do you want to train an initial model? 💪🏽 No
No problem 👍🏼. You can also train a model later by going to the project directory and running 'rasa train'.
```

## Run a Project
```
docker run --rm -it -v "./newsletter:/app" --name rasa -p 5005:5005 -p 5006:5006 --entrypoint /bin/bash rasa/rasa:3.6.6-full
```

## Init a POC

- newsletter service: get client email and reply
` create by interactive mode`

* up by interactive mode
```
# docker run --rm -it -v "./example/newsletter:/app" --name newsletter-poc -p 5005:5005 -p 5006:5006 --entrypoint /bin/bash rasa/rasa:3.6.6-full
# rasa interactive
```

```terminal
.
.
.
The configuration for pipeline and policies was chosen automatically. It was written into the config file at 'config.yml'.
.
.
.
2023-08-25 16:28:07 INFO     rasa.nlu.featurizers.sparse_featurizer.count_vectors_featurizer  - 697 vocabulary items were created for text attribute.
2023-08-25 16:28:07 INFO     rasa.engine.training.hooks  - Finished training component 'CountVectorsFeaturizer'.
2023-08-25 16:28:07 INFO     rasa.engine.training.hooks  - Starting to train component 'DIETClassifier'.
Epochs: 100%|██████████████████████████████████████████████████████████| 100/100 [00:16<00:00,  5.91it/s, t_loss=1.11, i_acc=1]
.
.
.
Bot loaded. Visualisation at http://localhost:5006/visualization.html .
Type a message and press enter (press 'Ctrl-c' to exit).
? Your input -> hi
? Your NLU model classified 'hi' with intent 'greet' and there are no entities, is this correct? Yes
------
Chat History

 #    Bot                        You        
────────────────────────────────────────────
 1    action_listen                         
────────────────────────────────────────────
 2                                       hi 
                         intent: greet 1.00 


Current slots: 
        session_started_metadata: None

------
? The bot wants to run 'utter_greet', correct? Yes
/opt/venv/lib/python3.10/site-packages/rasa/server.py:860: FutureWarning: The "POST /conversations/<conversation_id>/execute" endpoint is deprecated. Inserting actions to the tracker externally should be avoided. Actions should be predicted by the policies only.
  rasa.shared.utils.io.raise_warning(
------
Chat History



 #    Bot                            You        
────────────────────────────────────────────────
 1    action_listen                             
────────────────────────────────────────────────
 2                                           hi 
                             intent: greet 1.00 
────────────────────────────────────────────────
 3    utter_greet 1.00                          
      Hey! How are you?                         
------
Current slots: 
        session_started_metadata: None

? The bot wants to run 'action_listen', correct? Yes
? Your input -> 

```

* create intent by interactive mode

```terminal
? Your input -> i want to subscript the news letter
? Your NLU model classified 'i want to subscript the news letter' with intent 'mood_great' and there are no entities, is this c
orrect? No
? What intent is it? <create_new_intent>
? Please type the intent name: subcript_news_letter
? Please mark the entities using [value](type) notation i want to subscript the [news letter](service)
------
Chat History



 #    Bot                                                        You        
────────────────────────────────────────────────────────────────────────────
 1    action_listen                                                         
────────────────────────────────────────────────────────────────────────────
 2                                                                       hi 
                                                         intent: greet 1.00 
────────────────────────────────────────────────────────────────────────────
 3    utter_greet 1.00                                                      
      Hey! How are you?                                                     
      action_listen                                                         
────────────────────────────────────────────────────────────────────────────
 4                           i want to subscript the [news letter](service) 
                                          intent: subcript_news_letter 1.00 
Current slots: 
        session_started_metadata: None

------
? The bot wants to run 'utter_happy', correct?
```

* create action by interactive mode
```terminal
? The bot wants to run 'utter_happy', correct? No
------
Chat History



 #    Bot                                                        You        
────────────────────────────────────────────────────────────────────────────
 1    action_listen                                                         
────────────────────────────────────────────────────────────────────────────
 2                                                                       hi 
                                                         intent: greet 1.00 
────────────────────────────────────────────────────────────────────────────
 3    utter_greet 1.00                                                      
      Hey! How are you?                                                     
      action_listen                                                         
────────────────────────────────────────────────────────────────────────────
 4                           i want to subscript the [news letter](service) 
                                          intent: subcript_news_letter 1.00 
------
Current slots: 
        session_started_metadata: None

? What is the next action of the bot? <create new action>
? Please type the action name: utter_subcript_news_letter
? Please type the message for your new bot response 'utter_subcript_news_letter': what is your email address?
Thanks! The bot will now run utter_subcript_news_letter.
------
Chat History



 #    Bot                                                                 You        
─────────────────────────────────────────────────────────────────────────────────────
 1    action_listen                                                                  
─────────────────────────────────────────────────────────────────────────────────────
 2                                                                                hi 
                                                                  intent: greet 1.00 
─────────────────────────────────────────────────────────────────────────────────────
 3    utter_greet 1.00                                                               
      Hey! How are you?                                                              
      action_listen                                                                  
─────────────────────────────────────────────────────────────────────────────────────
 4                                    i want to subscript the [news letter](service) 
                                                   intent: subcript_news_letter 1.00 
─────────────────────────────────────────────────────────────────────────────────────
 5    utter_subcript_news_letter                                                     
Current slots: 
        session_started_metadata: None

------
? The bot wants to run 'action_listen', correct? Yes
? Your input ->

```

* create eneity by interactive mode
```terminal
? Your input -> my mail is greatmail@mail.home.tw
? Your NLU model classified 'my mail is greatmail@mail.home.tw' with intent 'mood_great' and there are no entities, is this cor
rect? No
? What intent is it? <create_new_intent>
? Please type the intent name: inform_email
? Please mark the entities using [value](type) notation my mail is [greatmail@mail.home.tw](email)
------
Chat History



 #    Bot                                                                 You        
─────────────────────────────────────────────────────────────────────────────────────
 1    action_listen                                                                  
─────────────────────────────────────────────────────────────────────────────────────
 2                                                                                hi 
                                                                  intent: greet 1.00 
─────────────────────────────────────────────────────────────────────────────────────
 3    utter_greet 1.00                                                               
      Hey! How are you?                                                              
      action_listen                                                                  
─────────────────────────────────────────────────────────────────────────────────────
 4                                    i want to subscript the [news letter](service) 
                                                   intent: subcript_news_letter 1.00 
─────────────────────────────────────────────────────────────────────────────────────
 5    utter_subcript_news_letter                                                     
      action_listen                                                                  
─────────────────────────────────────────────────────────────────────────────────────
 6                                        my mail is [greatmail@mail.home.tw](email) 
                                                           intent: inform_email 1.00 
Current slots: 
        session_started_metadata: None

------
? The bot wants to run 'utter_happy', correct? No
------
Chat History



 #    Bot                                                                 You        
─────────────────────────────────────────────────────────────────────────────────────
 1    action_listen                                                                  
─────────────────────────────────────────────────────────────────────────────────────
 2                                                                                hi 
                                                                  intent: greet 1.00 
─────────────────────────────────────────────────────────────────────────────────────
 3    utter_greet 1.00                                                               
      Hey! How are you?                                                              
      action_listen                                                                  
─────────────────────────────────────────────────────────────────────────────────────
 4                                    i want to subscript the [news letter](service) 
                                                   intent: subcript_news_letter 1.00 
─────────────────────────────────────────────────────────────────────────────────────
 5    utter_subcript_news_letter                                                     
      action_listen                                                                  
─────────────────────────────────────────────────────────────────────────────────────
 6                                        my mail is [greatmail@mail.home.tw](email) 
                                                           intent: inform_email 1.00 
Current slots: 
        session_started_metadata: None

------
? What is the next action of the bot? <create new action>
? Please type the action name: utter_reply_subscript_mail_address
? Please type the message for your new bot response 'utter_reply_subscript_mail_address': Done! I will send news letter to {ema
il}!
Thanks! The bot will now run utter_reply_subscript_mail_address.

------
Chat History



 #    Bot                                                                         You        
─────────────────────────────────────────────────────────────────────────────────────────────
 1    action_listen                                                                          
─────────────────────────────────────────────────────────────────────────────────────────────
 2                                                                                        hi 
                                                                          intent: greet 1.00 
─────────────────────────────────────────────────────────────────────────────────────────────
 3    utter_greet 1.00                                                                       
      Hey! How are you?                                                                      
      action_listen                                                                          
─────────────────────────────────────────────────────────────────────────────────────────────
 4                                            i want to subscript the [news letter](service) 
                                                           intent: subcript_news_letter 1.00 
─────────────────────────────────────────────────────────────────────────────────────────────
 5    utter_subcript_news_letter                                                             
      action_listen                                                                          
─────────────────────────────────────────────────────────────────────────────────────────────
 6                                                my mail is [greatmail@mail.home.tw](email) 
                                                                   intent: inform_email 1.00 
─────────────────────────────────────────────────────────────────────────────────────────────
 7    utter_reply_subscript_mail_address                                                     
------
Current slots: 
        session_started_metadata: None

? The bot wants to run 'action_listen', correct? Yes
```

* export by interactive mode
```terminal
? The bot wants to run 'action_listen', correct? Yes
? Your input ->                                                                                                                

Cancelled by user

? Do you want to stop? Export & Quit
? Export stories to (if file exists, this will append the stories) data/stories.yml
? Export NLU data to (if file exists, this will merge learned data with previous training examples) data/nlu.yml
? Export domain file to (if file exists, this will be overwritten) domain.yml
/opt/venv/lib/python3.10/site-packages/rasa/shared/utils/io.py:99: UserWarning: The following duplicated intents have been found across multiple domain files: greet
  More info at https://rasa.com/docs/rasa/domain
2023-08-25 16:40:47 INFO     rasa.core.training.interactive  - Successfully wrote stories and NLU data
2023-08-25 16:40:47 INFO     rasa.core.training.interactive  - Killing Sanic server now.
```

## todo
- Form
- Custom Actions
- Rule
