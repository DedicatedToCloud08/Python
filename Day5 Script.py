#!/usr/bin/env python3

"""

This is a day 5 script which will help us understand how to load files correctly and get deeper understanding of
how several other libraries operate

"""

import json
from pathlib import Path


#### Functions

## To load the file

def load_file(file_path: Path) -> dict:
    if file_path.exists():
        with open(file_path, "r") as file:
            return json.load(file)
    else:
        return {}

## To print the loaded file

def print_file(resource_json: dict):
    for name, details in resource_json.items():
        print(f"{name} : {details['type']} {details['status']} ")
    print(f"Above are the current list of resources!")


## To Save the changes we made into the file

def save_file(file_path: Path, resources: dict):
    with open(file_path, "w") as file:
        json.dump(resources, file, indent=4)
    print("The file update is completed!")

def choce_checker(prompt: str) -> str:
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ["stopped", "running"]:
            return user_input
        else:
            print("Please enter a valid state (stopped/running)")



if __name__ == "__main__":

    path = Path("day5test.json")
    resource = load_file(path)

    ## Dummy resource if resource file is fallbacked to empty
    if not resource:
        resource = {
            "web-server-1": {"type": "EC2", "status": "running"},
            "db-server-1": {"type": "RDS", "status": "stopped"},
            "cache-1": {"type": "Redis", "status": "running"}
        }

    print_file(resource)

    while True:

        choice = input("Please input the resource you want to change the state from (stopping -> Running or vice-versa): or to stop say 'exit'").strip().lower()

        if choice == "exit":
            print("Thanks for using this service! have a nice day")
            break

        if choice in resource:
            resource[choice]['status'] = "stopped" if resource[choice]['status'] == "running" else "running"
            print(f"The status of {choice} is now updated to {resource[choice]['status']}")
            save_file(path, resource)
        else:
            print("resource not found!!!!")
        