
```
docker build -t siredmar/mqttrpi .
docker push siredmar/mqttrpi:latest
docker run -e MQTT_SERVER="broker.mqttdashboard.com" -e MQTT_PORT=1883 -e MQTT_TOPIC="ci4rail" siredmar/mqttrp
```

