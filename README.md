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

#### newsletter service: get client email and reply
`create by interactive mode`
[here](./example/newsletter/README-example-newsletter.md)



## todo
- Form
- Custom Actions
- Rule



#### manually to fintune
```
docker run --rm -it -v "actionsServer:/app" --name rasa -p 5005:5005 -p 5006:5006 --entrypoint /bin/bash rasa/rasa:3.6.6-full

docker run --rm -it -v ".actionsServer:/app" --name rasa -p 5005:5005 -p 5006:5006 --entrypoint /bin/bash rasa/rasa:3.6.6-full
docker exec -it rasa /bin/bash
```


#### testing service
- up service
```
docker-compose up
```

- ask bot by cmd
````
curl -o output.txt -X POST -H "Content-Type: application/json; charset=UTF-8" -d '{"sender": "user-001","message": "早安"}'  http://127.0.0.1:5005/webhooks/rest/webhook && echo -e "$(<output.txt)"
curl -o output.txt -X POST -H "Content-Type: application/json; charset=UTF-8" -d '{"sender": "user-001","message": "昆蟲是甚麼?"}'  http://127.0.0.1:5005/webhooks/rest/webhook && echo -e "$(<output.txt)"
curl -o output.txt -X POST -H "Content-Type: application/json; charset=UTF-8" -d '{"sender": "user-001","message": "是的"}'  http://127.0.0.1:5005/webhooks/rest/webhook && echo -e "$(<output.txt)"
```

curl -o output.txt -X POST -H "Content-Type: application/json; charset=UTF-8" -d '{"sender": "user-001","message": "昆蟲 八隻腳"}'  https://fuzzy-space-eureka-69r6vg7wqwrc5x9g-5005.app.github.dev/webhooks/rest/webhook/ && echo -e "$(<output.txt)"

curl -o output.txt -X POST -H "Content-Type: application/json; charset=UTF-8" -d '{"sender": "user-001","message": "昆蟲是甚麼"}'  https://fuzzy-space-eureka-69r6vg7wqwrc5x9g-5005.app.github.dev/webhooks/rest/webhook/ && echo -e "$(<output.txt)"
