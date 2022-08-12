import paho.mqtt.client as mqtt

def client_on_connect(client, data, flags, return_code):
   if return_code:
      print("Could not connect to host \"" + str(client._host) + "\"!\n")
   else:
      print("Successfully connected to host \"" + str(client._host) + "\"!\n")
   return 

def client_on_disconnect(client, data, return_code):
   if return_code:
      print("Unexpected disconnection from host \"" + str(client._host) + "\"!\n")
   else:
      print("Successfully disconnected from host \"" + str(client._host) + "\"!\n")
   return 

def client_new(host, port = 1883):
   import time
   client = mqtt.Client()
   client.on_connect = client_on_connect
   client.on_disconnect = client_on_disconnect
   client.connect(host, port)
   if not client.is_connected():
      client.reconnect()
   client.loop_start()
   time.sleep(0.1)
   return client

def client_delete(client):
   client.loop_stop()
   client.disconnect()
   return

def client_publish(client, topic, message, qos = 1):
   msg = client.publish(topic = topic, payload = message, qos = qos)
   msg.wait_for_publish()
   print("Published message \"" + str(message) + "\" to topic \"" + str(topic) + "\"!\n")
   return

def readline():
   s = input()
   print()
   return s

def main():
   client1 = client_new(host = "broker.hivemq.com")
   while True:
      print("Enter text or a blank line to finish:")
      s = readline()
      if s:
         client_publish(client = client1, topic = "yrgo/com", message = s) 
      else:
         break
   client_delete(client1)
   return 

if __name__ == "__main__":
   main()
