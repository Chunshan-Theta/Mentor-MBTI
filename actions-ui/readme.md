docker run --rm -it -v "actionsServer:/app" --name rasa -p 5005:5005 -p 5006:5006 --entrypoint /bin/bash rasa/rasa:3.6.6-full

docker run --rm -it -v "./botServer:/app" --name rasa -p 5005:5005 -p 5006:5006 --entrypoint /bin/bash rasa/rasa:3.6.6-full

docker exec -it actions-ui_rasa-actionServer_1 /bin/bash