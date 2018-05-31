import re
import paho.mqtt.client as mqtt
import aprs

regexMsg = r":WM(\w*){(\d)" #Filtert die Nachrichten aus dem APRS Paket, danke an Thomas Helmke für den Ausdruck
regexCalls = r"^(\w*).([0-9]*)" #Filtert das Rufzeichen raus

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    

def receivedAprsFrameCallback(msg):
    callsign = ""
    datamsg = ""    

    print("\n Received" + str(msg));
    matches = re.finditer(regexMsg, str(msg), re.MULTILINE)
    for matchNum, match in enumerate(matches):
        print("\n Msg: " + match.group(1));
        datamsg = str(match.group(1))
    matches = re.finditer(regexCalls, str(msg), re.MULTILINE)
    for matchNum, match in enumerate(matches):
        print("\n Callsign: " + match.group(1));
        callsign = str(match.group(1))
    if datamsg and callsign:
       client.publish(str(callsign), (datamsg), 0, False)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)
a = aprs.TCP(str.encode(mycallsign), str.encode(mypasscode))
a.start()
a.receive(callback=receivedAprsFrameCallback)

client.loop_forever()
