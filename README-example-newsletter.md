# rasa - newsletter service



## up by interactive mode
`# docker run --rm -it -v "./example/newsletter:/app" --name newsletter-poc -p 5005:5005 -p 5006:5006 --entrypoint /bin/bash rasa/rasa:3.6.6-full`

`# rasa interactive`

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

## create intent by interactive mode

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

## create eneity by interactive mode
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

## export by interactive mode
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


## add more example to training
- data/nlu.yml
```
- intent: subcript_news_letter
  examples: |
    - i want to subscript the [news letter](service)
    - yes, I'm so good. could I have a [newsletter](service) service?
    - subscript
    - [newsletter](service) please
    - I want to subscript the [newsletter](service) service
- intent: inform_email
  examples: |
    - my mail is [greatmail@mail.home.tw](email)
    - yes,  My email address is [ThetaWany@greatmail.com.tw](email)
    - [boyboy@gmail.com.tw](email)
    - Please send to [coolguy2023@hotmail.com](email)
```

- data/stories.yml
```
- story: interactive_story_1
  steps:
  - intent: subcript_news_letter
  - action: utter_subcript_news_letter
  - intent: inform_email
  - action: utter_reply_subscript_mail_address
```

- domain.yml
```
entities:
- email
- service

slots:
  email:
    type: text
    mappings:
    - type: from_entity
      entity: email
  service:
    type: text
    mappings:
    - type: from_entity
      entity: service

actions:
- utter_subcript_news_letter
- utter_reply_subscript_mail_address
```