#!/usr/bin/env python3

"""
This is a demo script
"""

def greet(name: str) -> str:
    return f"Hello, {name}!. welcome to my first script."

if __name__ == "__main__":
    user = input("Enter your name:")
    print(greet(user))

