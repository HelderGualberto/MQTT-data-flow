import paho.mqtt.client as mqtt
import sys, time
import multiprocessing

username = ""
userpass = ""
broker_uri = ""


def start_publishing(data_flow,data_duration,connection_param):
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message
	client.username_pw_set(connection_param[0],connection_param[1])
	client.connect(connection_param[2], 1883, 60)

	#define the payload to send
	payload = "message to send"

	#define the topic to publish messages
	topic = "/mqtt/analyser"

	time_to_sleep = 1/float(data_flow)
	for i in range(0,int(data_flow)*int(data_duration)):
		client.publish(topic,payload,qos=1,retain=False)
		print "sleep: " + str(time_to_sleep)
		time.sleep(time_to_sleep)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
	print "msg"


#Array that contains the informations about connection to the server.
#MQTT server, user and pass
connection_param = [None]*3
connection_param[0] = username
connection_param[1] = userpass
connection_param[2] = broker_uri


#The data_flow is defined by number of messages per second
data_flow = int(sys.argv[1])

#The time that data will stay sending
data_duration = int(sys.argv[2])

#The data_points are the number of "simulated devices" that will send the messagens simultaneously
if len(sys.argv) > 3:
	data_points = int(sys.argv[3])
else:
	data_points = 1

for i in range(0,data_points):
	if __name__ == '__main__':	
		p = multiprocessing.Process(target=start_publishing,args=(data_flow,data_duration,connection_param),)
		p.start()
