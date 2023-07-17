from firebase import firebase
import RPi.GPIO as GPIO

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Suppress GPIO warnings
GPIO.setwarnings(False)

# Set up GPIO pins for controlling lights
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

# Turn off all lights initially
GPIO.output(2, GPIO.HIGH)
GPIO.output(3, GPIO.HIGH)
GPIO.output(4, GPIO.HIGH)
GPIO.output(15, GPIO.HIGH)

# Initialize Firebase application
firebase_app = firebase.FirebaseApplication('YOUR_FIREBASE_APPLICATION_URL')

while True:
    # Read the status of lightOne from Firebase
    light_one = firebase_app.get('/light', 'lightOne')
    if light_one == 'on':
        GPIO.output(2, GPIO.LOW)  # Turn on lightOne
    else:
        GPIO.output(2, GPIO.HIGH)  # Turn off lightOne

    # Read the status of lightTwo from Firebase
    light_two = firebase_app.get('/light', 'lightTwo')
    if light_two == 'on':
        GPIO.output(3, GPIO.LOW)  # Turn on lightTwo
    else:
        GPIO.output(3, GPIO.HIGH)  # Turn off lightTwo

    # Read the status of lightThree from Firebase
    light_three = firebase_app.get('/light', 'lightThree')
    if light_three == 'on':
        GPIO.output(4, GPIO.LOW)  # Turn on lightThree
    else:
        GPIO.output(4, GPIO.HIGH)  # Turn off lightThree

    # Read the status of lightFour from Firebase
    light_four = firebase_app.get('/light', 'lightFour')
    if light_four == 'on':
        GPIO.output(15, GPIO.LOW)  # Turn on lightFour
    else:
        GPIO.output(15, GPIO.HIGH)  # Turn off lightFour

    print('-------------------------------')

GPIO.cleanup()
