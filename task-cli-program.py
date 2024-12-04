import argparse
import json
import os
from datetime import datetime

TASK_FILE = os.path.abspath("./data.json")
parser = argparse.ArgumentParser()

# initialize
input_id = 0
description = ""
status = ""
createdAt = datetime.now()
updatedAt = datetime.now()


def add_data():
    # input arguments through terminal
    parser.add_argument("-n", "--name", type=str, help="name input")
    parser.add_argument("-s", "--status", type=str, help="status input")
    
    args = parser.parse_args()


    data = {
        "input_id": 1,
        "description": args.name,
        "status": args.status,
        "createdAt": createdAt.isoformat(),
        "updatedAt": updatedAt.isoformat()
    }

    # file not exists then create one
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w") as file:
            json.dump({"data": []}, file, indent=4)
            print("No existing data found, creating new file.")

    # data handling part
    else:
        with open(TASK_FILE, "r") as file:
            try:
                json_data = json.load(file)
            except json.JSONDecodeError:
                json_data = {"data": []}

        json_data["data"].append(data)

        with open(TASK_FILE, "w") as file:
            json.dump(json_data, file, indent=4)

        print(f"Data added successfully: {data}")


if __name__ == "__main__":
    add_data()