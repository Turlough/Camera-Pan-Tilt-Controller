import paho.mqtt.client as mqtt
from flask import Flask, render_template, request

app = Flask(__name__)
mqtt_client = mqtt.Client()

# Replace these with your own configuration
host = '172.16.92.200'
port = 1883
topic = 'pan_tilt_controller'
username = 'turlough'
password = 'b00lab00la'

# Create a dictionary for pin number, name, and pin state:

sliders = {
    'left': {'direction': 'forward', 'value': 90},
    'right': {'direction': 'forward', 'value': 90}
}
# Put the pin dictionary into the template data dictionary:
templateData = {
    'sliders': sliders
}


@app.route("/")
def main():
    """Display the main page, with no servo data yet"""
    mqtt_client.publish(topic, 'server message')
    return render_template('ws_controller.html', **templateData)


@app.route("/<left>/<right>")
def slider_action(left, right):
    """
    Display the main page, with servos in position indicated by 'left' and 'right'.
    Also publish 'left','right' via mqtt.
    """
    sliders['left']['value'] = left
    sliders['right']['value'] = right
    mqtt_client.publish(topic, left + ',' + right)

    # Along with the pin dictionary, put the message into the template data dictionary:
    template_data = {
        'sliders': sliders
    }

    return render_template('ws_controller.html', **template_data)


def start_mqtt():
    """Connect the mqtt client so it's ready to publish"""
    mqtt_client.username_pw_set(username, password)
    mqtt_client.connect(host, port, 60)
    mqtt_client.loop_start()


if __name__ == "__main__":
    start_mqtt()
    app.run(host='0.0.0.0', port=8081, debug=True)
