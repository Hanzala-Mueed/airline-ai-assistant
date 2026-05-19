import json

CHAT_HISTORY_FILE = "app/data/chat_history.json"

def load_chat_history():
    try:
        with open(CHAT_HISTORY_FILE, "r") as file:
            return json.load(file)

    except:
        return []


def save_chat_history(messages):
    with open(CHAT_HISTORY_FILE, "w") as file:
        json.dump(messages, file, indent=4)