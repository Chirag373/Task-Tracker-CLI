import argparse
import os

TASK_FILE = os.path.abspath("./data.json")

def add_data():
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w") as file:
            pass


if __name__ == "__main__":
    add_data()