# Home Automation with Raspberry Pi

This project enables home automation using Raspberry Pi and Firebase. It allows controlling lights connected to the Raspberry Pi GPIO pins through a mobile application that is integrated with Firebase.

## Prerequisites

- Raspberry Pi with RPi.GPIO library installed
- Mobile application integrated with Firebase for controlling lights

## Installation

1. Connect the Raspberry Pi and set up the required GPIO pins (2, 3, 4, and 15) for controlling the lights.

2. Install the RPi.GPIO library on your Raspberry Pi if not already installed:
   ```
   pip install RPi.GPIO
   ```

3. Clone or download the project files to your Raspberry Pi.

4. Open the Python script file `Home_Automation_RaspberryPi.py` and replace `'YOUR_FIREBASE_APPLICATION_URL'` with the URL of your Firebase application.

## Usage

1. Run the Python script:
   ```
   python Home_Automation_RaspberryPi.py
   ```

2. The script will initialize the GPIO pins and turn off all lights.

3. The script will continuously monitor the Firebase database for changes in the status of the lights.

4. Any updates made to the lights' status through the mobile application connected to Firebase will be reflected in the Raspberry Pi GPIO pins, turning the lights on or off accordingly.

5. Check the console for status updates and ensure that the lights are being controlled based on the Firebase database.

## Mobile Application Integration

1. Develop or configure a mobile application that integrates with Firebase for controlling the lights.

2. Ensure that the mobile application can update the `/light` node in the Firebase database with the desired status of each light (e.g., 'on' or 'off').

3. The Raspberry Pi script will monitor this Firebase database node and control the lights accordingly.

## Customization

- You can customize the GPIO pin numbers for controlling the lights by modifying the `GPIO.setup` and `GPIO.output` lines in the script.
- Ensure that the mobile application is integrated with Firebase correctly and follows the same structure for controlling the lights in the Firebase database.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).