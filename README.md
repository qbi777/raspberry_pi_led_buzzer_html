# raspberry_pi_led_buzzer_html
![raspberry_pi_led_buzzer](https://github.com/qbi777/raspberry_pi_led_buzzer_html/assets/123941775/11c8fa44-b86d-4cd4-b2f8-934608a4cfe3)

Raspberry Pi LED and Buzzer Control with Flask This Python script allows you to control an LED and a buzzer using a Raspberry Pi through a web-based interface created with the Flask framework. The web page provides buttons to toggle the LED and the buzzer on and off.
![html_led_buzzer](https://github.com/qbi777/raspberry_pi_led_buzzer_html/assets/123941775/1a01ece4-04c0-4ac7-af61-f2063475fb0d)
Prerequisites
Before running this code, make sure you have the following components and software set up:

Raspberry Pi (any model with GPIO pins)
RPi.GPIO library (Python library for GPIO control)
Python 3
Flask library (for creating the web interface)

Explanation:

This Python script demonstrates how to control an LED and a buzzer using a Raspberry Pi with a web-based interface created using the Flask framework. It allows you to toggle the LED and the buzzer on and off by accessing specific URLs in your web browser.

The script uses the RPi.GPIO library for Raspberry Pi GPIO control and the Flask library for creating a web server.
It sets up two GPIO pins (led_pin and buzzer_pin) as outputs for controlling the LED and buzzer.
The Flask app has two routes:
/: This route renders an HTML template called index.html, which contains buttons to toggle the LED and the buzzer.
/toggle_led and /toggle_buzzer: These routes are used to toggle the LED and buzzer, respectively, by changing the state of the GPIO pins.
