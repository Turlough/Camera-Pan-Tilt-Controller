import paho.mqtt.client as mqtt
from flask import Flask, render_template, request
app = Flask(__name__)

# Replace these with your own configuration
host = '172.16.92.200'
port = 1883
topic = 'pan_tilt_controller'
username = 'turlough'
password = 'b00lab00la'

mqttc=mqtt.Client()
mqttc.connect(host, port, 60)
mqttc.loop_start()

# Create a dictionary for pin number, name, and pin state:

sliders = {
    'left':{'direction':'forward', 'value':90},
    'right':{'direction':'forward', 'value':90}
}
# Put the pin dictionary into the template data dictionary:
templateData = {
   'sliders' : sliders
   }


@app.route("/")
def main():
   # Pass the template data into the template main.html and return it to the user
   mqttc.publish(topic, 'server message')
   return render_template('ws_controller.html', **templateData)

@app.route("/<left>/<right>")
def sliderAction(left, right):
    sliders['left']['value'] = left
    sliders['right']['value'] = right
    mqttc.publish(topic, left + ',' + right)


    # Along with the pin dictionary, put the message into the template data dictionary:
    templateData = {
        'sliders': sliders
    }

    return render_template('ws_controller.html', **templateData)



mqttc=mqtt.Client()
mqttc.username_pw_set(username, password)
mqttc.connect(host, port, 60)
mqttc.loop_start()


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)