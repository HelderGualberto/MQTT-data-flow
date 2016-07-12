# MQTT-data-flow
This repository contains a python script that connects to a MQTT Broker and send some dummy data to analyse the escalability of the MQTT Broker

# Configuring the Server
Before you execute the script you need to edit the code and change the username, pass and MQTT broker that you will use.

# Script Parameters
The script has 2 required parameters, and one optional. These are:
(required) First parameter - The number of messages that will be send in one second. (That can be called data flow) 
(required) Second parameter - The time while the client will stay sending messages, with the previous data flow
(optional) Third parameter - The number of clients that will be sending messages simultaneously (default value is 1)

# Example of use
python mqtt-flow-mesurer.py 10 3 5

This exemple means that five clients will send 10 messeges per second over three seconds (The messagens will be send to the same mqtt topic)
