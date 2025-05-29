import json
import os

def save_to_json(data_entry):
    data_list = []
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            try:
                data_list = json.load(f)
                if not isinstance(data_list, list):
                    data_list = []
            except json.JSONDecodeError:
                data_list = []
    
    data_list.append(data_entry)
    with open("data.json", "w") as f:
        json.dump(data_list, f, indent=4)