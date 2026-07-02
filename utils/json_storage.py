import json
import os
from config import DATA_FILE, MOVEMENTS_FILE

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"products": []}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_movements():
    if not os.path.exists(MOVEMENTS_FILE):
        return {"movements": []}
    with open(MOVEMENTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_movements(data):
    with open(MOVEMENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)