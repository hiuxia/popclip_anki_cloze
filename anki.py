import json
import os
from datetime import datetime
import requests

# Get the text from POPCLIP_TEXT environment variable
text = os.environ.get("POPCLIP_TEXT", "")
if not text:
    exit()

# Get current date in YYYY-MM-DD format
current_date = datetime.now().strftime("%Y-%m-%d")

# Prepare the data payload
data = {
    "action": "guiAddCards",
    "version": 6,
    "params": {
        "note": {
            "deckName": "Default",
            "modelName": "Cloze",
            "fields": {"Text": text},
            "tags": ["popclip", current_date],
        }
    },
}

# Send POST request to AnkiConnect
response = requests.post(
    "http://localhost:8765", headers={"Content-Type": "application/json"}, json=data
)
