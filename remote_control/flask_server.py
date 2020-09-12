import paho.mqtt.client as mqtt
from flask import Flask, render_template, request
from json_loader import JsonLoader

app = Flask(__name__)
mqtt_client = mqtt.Client()
topic = ''
config = JsonLoader()


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
    :param tilt: Up down motion, values 0-180
    :param pan: Left right motion, values 0-180
    """
    global topic

    sliders['tilt']['value'] = tilt
    sliders['pan']['value'] = pan
    mqtt_client.publish(topic, tilt + ',' + pan)

    # Along with the pin dictionary, put the message into the template data dictionary:
    template_data = {
        'sliders': sliders
    }

    return render_template('ws_controller.html', **template_data)


def start_mqtt():
    """Connect the mqtt client so that it's ready to publish"""
    global topic
    c = config.from_file('mqtt_config.json')
    topic = c.topic
    mqtt_client.username_pw_set(c.username, c.password)
    mqtt_client.connect(c.host, c.port, 60)
    mqtt_client.loop_start()


if __name__ == "__main__":
    start_mqtt()
    app.run(host='0.0.0.0', port=8081, debug=True)
