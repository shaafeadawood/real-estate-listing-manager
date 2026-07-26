import json
import os

DATA_FILE = "listings.json"

def load_listings():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_listings(listings):
    with open(DATA_FILE, "w") as file:
        json.dump(listings, file, indent=4)