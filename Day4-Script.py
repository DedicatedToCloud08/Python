#!/usr/bin/env python3

"""
This is a day 4 Script what has Dictionaries and nested dictionaries

"""

def dictbreaker(choice: dict):
    for name, details in choice.items():
        print(f"{name} : {details['type']}")


if __name__ == "__main__":
    Resources = {"web-server-1": {"type": "EC2", "status": "running"},
        "db-server-1": {"type": "RDS", "status": "stopped"},
        "cache-1": {"type": "Redis", "status": "running"}}
    
    dictbreaker(Resources)

    while True:
        choice = input("Enter a resource name to know the status: (to cancel type 'exit') ").strip().lower()
        if choice == "exit":
            break 
        if choice in Resources:
            print(f"The current status of {choice} is {Resources[choice]['status']} and the resource type is {Resources[choice]['type']}")
        else:
            dictbreaker(Resources)
            print("Resource not found")
        
    print("Thanks for using our service!")