FROM balenalib/raspberrypi3-alpine-python:3-3.12

COPY . /app
WORKDIR /app
RUN chmod +x mqtt.py
RUN pip3 install -r requirements.txt

ENTRYPOINT ["/app/mqtt.py"]
