#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import os
import time

# This is the Publisher

client = mqtt.Client()
client.connect(os.environ['MQTT_SERVER'], int(os.environ['MQTT_PORT']), 60)
i = 0
while True:
	client.publish(os.environ['MQTT_TOPIC'], str(i));
	i = i + 1
	time.sleep(1)
client.disconnect();
