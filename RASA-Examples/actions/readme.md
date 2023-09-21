1. 
> docker run --rm -it -v "./actionsServer:/app" --name rasa -p 5005:5005 -p 5006:5006 --entrypoint /bin/bash rasa/rasa:3.6.6-full
> rasa run actions

2.
> docker exec -it rasa /bin/bash
> rasa shell