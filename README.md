# Camera Pan-Tilt Controller
MQTT control system for a servo controlled Pan-Tilt mount.
Do NOT use this for a security system or expose it publicly, use it on your internal network only.
* The _pi_ directory contains the code for controlling the camera; copy it to some directory on your Raspberry Pi. 
Camera service is not included, I recommend [motioneye](https://pypi.org/project/motioneye/).
* The _remote control_ directory runs a cheap and cheerful Flask server (do NOT use this publicly, it is not secure). 
This provides a web page with a pair of sliders for manipulating the pan-tilt servos, which you can host elsewhere.
* _Remote control_ communicates with _pi_ using MQTT. They do not have to run on the same machine. 
The MQTT broker likewise can run on a separate machine. 
For testing, you can use a public sandbox broker, e.g. that at [eclipse.org](https://iot.eclipse.org/getting-started/#sandboxes)

