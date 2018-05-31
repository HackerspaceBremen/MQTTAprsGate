MQTT Aprs-IS Gate
This docker image routes aprs data sended to your entered callsign with message Prefix WM to the iot.eclipse.org server (changeable in app.py)

Use at your own risk, i do not guarantee if you break the law or anything else.

Installation

First enter your aprs-is credentials under config.sh

Build the container with:

docker build -t aprsbridge .

Run it with:

docker run aprsbridge:latest

You do NOT need to expose any ports.
