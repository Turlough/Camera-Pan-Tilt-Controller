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

sliders = {
    'tilt': {'direction': 'forward', 'value': 90},
    'pan': {'direction': 'forward', 'value': 90}
}

templateData = {
    'sliders': sliders
}


@app.route("/")
def main():
    """Display the main page, with no servo data yet"""
    mqtt_client.publish(topic, 'server message')
    return render_template('ws_controller.html', **templateData)


@app.route("/<tilt>/<pan>")
def slider_action(tilt, pan):
    """
    Re-display the main page, with servos in position indicated by 'tilt' and 'pan'.
    Also publish tilt and pan values via mqtt.

    This solution is a little janky, in that the entire page reloads (redirects in fact),
    when sliders are released, forcing a redraw of the camera view.
    @:param tilt: Up down motion, values 0-180
    @:param pan: Left right motion, values 0-180
    """
    sliders['tilt']['value'] = tilt
    sliders['pan']['value'] = pan
    mqtt_client.publish(topic, tilt + ',' + pan)

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
