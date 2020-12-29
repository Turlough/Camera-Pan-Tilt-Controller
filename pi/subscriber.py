"""
Python MQTT subsciber, using paho client.
Process incoming messages in 'on_message'. 
Expected message format is 'pan,tilt' where both values >0 and <180.
These represent target degrees for each servo
"""
import paho.mqtt.client as mqtt
from pan_tilt_controller import PanTiltController
from json_loader import JsonLoader

config = JsonLoader()
topic = ''

# define pins. On the Pi zero, pins 18 and 12 support PWM on a hardware level. We use 18 and 12 here.
controller = PanTiltController(pan_pin=18, tilt_pin=12)


def on_message(mosq, obj, msg):

    payload = msg.payload.decode("utf-8")
    try:
        (pan, tilt) = payload.split(',')
        p = int(pan)
        t = int(tilt)
        controller.pan(p)
        controller.tilt(t)
    except Exception as e:
        print(e)


def on_connect(client, userdata, flags, rc):

    print("Connected with result code " + str(rc))
    client.subscribe(topic, 0)


def main():
    global topic

    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect

    c = config.from_file('../mqtt_config.json')
    topic = c.topic

    client.username_pw_set(c.username, c.password)
    client.connect(c.host, c.port, 60)
    client.loop_forever()


if __name__ == '__main__':
    main()
