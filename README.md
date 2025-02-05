# ISS Overhead Notifier

This project notifies you via email when the International Space Station (ISS) is near your location during daytime. It uses real-time data from APIs to determine:
- Sunrise and sunset times for your location.
- The current position of the ISS.

## How It Works

1. The script retrieves sunrise and sunset times from the [Sunrise-Sunset API](https://sunrise-sunset.org/api) to determine the daytime window.
2. It checks the ISS's position by querying the [Open Notify ISS API](http://api.open-notify.org/iss-now.json).
3. If the ISS is within a 5-degree range of your location and it is currently daytime, an email notification is sent using SMTP.

## Setup

1 **Install dependencies:**
    Run:
    ```
    pip install -r requirements.txt
    ```

3. **Configure Environment Variables:**
    Create a `.env` file (this file is already ignored by Git due to `.gitignore`) and define the following variables:
    ```
    MY_EMAIL=your_email@example.com
    MY_PASSWORD=your_email_password
    RECEIVER=receiver_email@example.com
    ```
    Make sure to use valid credentials and consider using an app-specific password if your email provider requires it.

## Running the Project

Simply run the main script:
```
python main.py
```
The script will check for the ISS position every 60 seconds and send an email if all conditions are met.

## Notes

- Ensure that you have a stable internet connection.
- The script is set to run indefinitely. Use `Ctrl + C` to stop the process.
