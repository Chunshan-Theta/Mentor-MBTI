
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