# Camera Pan-Tilt Controller
MQTT control system for a servo controlled Pan-Tilt mount.

It is designed in multiple standalone modules, which means that, 
for example, the servos can be controlled by any MQTT publisher, 
not just that provided in the _Remote Control_ module.

This is not really intended to be a security system, it's for use on internal networks
and messing around with.

## Modules
* The _pi_ directory contains the code for controlling the camera; copy it to some directory on your Raspberry Pi.
* _vid stream_ streams camera output to the specified PORT. 
* The _remote control_ directory runs a cheap and cheerful Flask server (do NOT use this publicly, it is not secure). 
This provides a web page with a pair of sliders for manipulating the pan-tilt servos, 
  which you can host elsewhere. The video stream is that provided by _vid stream_ above.
* _Remote control_ communicates with _pi_ using MQTT. They do not have to run on the same machine. 
The MQTT broker likewise can run on a separate machine. 
For testing, you can use a public sandbox broker, 
  e.g. that at [eclipse.org](https://iot.eclipse.org/getting-started/#sandboxes)
  
## Instructions
1. Edit the config file (mqtt_config.json) to use a valid MQTT server (e.g. at eclipse.org, or your own)
1. Calibrate the servos
1. Start the video stream from _vid stream/main.py_
1. Start the flask server in _Remote Control/flask server.py_
1. Start the MQTT subscriber in _pi/main.py_
1. Browse to the URL and port indicated in the config files with a web browser
1. Jiggle the controls. 
1. Success!