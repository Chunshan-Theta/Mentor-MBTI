# rasa

## Init a Project
```
# docker run --rm -it -v "./[PROJECT NAME]:/app" --name [PROJECT NAME] rasa/rasa:3.6.6-full init

docker run --rm -it -v "./newsletter:/app" --name rasa rasa/rasa:3.6.6-full init
```

## Run a Project
```
docker run --rm -it -v "./newsletter:/app" --name rasa -p 5005:5005 -p 5006:5006 --entrypoint /bin/bash rasa/rasa:3.6.6-full
```
