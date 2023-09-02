import RPi.GPIO as GPIO
from flask import Flask, render_template

app = Flask(__name__)

led_pin = 17
buzzer_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(buzzer_pin, GPIO.OUT)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle_led')
def toggle_led():
    GPIO.output(led_pin, not GPIO.input(led_pin))
    return 'LED toggled'

@app.route('/toggle_buzzer')
def toggle_buzzer():
    GPIO.output(buzzer_pin, not GPIO.input(buzzer_pin))
    return 'Buzzer toggled'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
