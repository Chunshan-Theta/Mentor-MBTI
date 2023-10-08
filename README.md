# RASA
This is a mentor bot that can help be a recommander by rasa and LLM.

#### Demo service
- up service
```
docker-compose up
```

- ask bot by cmd
```
curl -o output.txt -X POST -H "Content-Type: application/json; charset=UTF-8" -d '{"sender": "user-001","message": "早安"}'  http://127.0.0.1:5005/webhooks/rest/webhook && echo -e "$(<output.txt)"
curl -o output.txt -X POST -H "Content-Type: application/json; charset=UTF-8" -d '{"sender": "user-001","message": "昆蟲是甚麼?"}'  http://127.0.0.1:5005/webhooks/rest/webhook && echo -e "$(<output.txt)"
curl -o output.txt -X POST -H "Content-Type: application/json; charset=UTF-8" -d '{"sender": "user-001","message": "是的"}'  http://127.0.0.1:5005/webhooks/rest/webhook && echo -e "$(<output.txt)"
```



- ask by web
```
http://localhost:80/
```


#### If you want to manually fintune
```
docker run --rm -it -v "actionsServer:/app" --name rasa -p 5005:5005 -p 5006:5006 --entrypoint /bin/bash rasa/rasa:3.6.6-full
```

or
```
docker run --rm -it -v ".actionsServer:/app" --name rasa -p 5005:5005 -p 5006:5006 --entrypoint /bin/bash rasa/rasa:3.6.6-full
```

or
```
docker exec -it rasa /bin/bash
```
