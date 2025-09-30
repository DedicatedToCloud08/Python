#!/usr/bin/env python3

"""
This is a day 2 script
"""

def Day2(name:str, age:int, is_devops:bool) -> str:

    ## A boolean ternary function
    answer = "A pro devops engineer" if is_devops else "cloud enthuiast"

    ##Integer operations
    next_year_age = age + 1

    return f"""
    Hello there following is your profile!
    Name: {name}
    Age: {age} Next year your age will be: {next_year_age}
    Role: {answer}

    Welcome to Bacchis world! :)
    """

def checkinput(prompt: str) -> bool:
    userinput = input(prompt).strip().lower()
    while True:
        if userinput in ["yes" "no"]:
            is_devops = (userinput == "yes")
            return is_devops
        else:
            print("wrong input please enter a valid value (yes/no)")


if __name__ == "__main__":
    name = input("Please enter your name: ")
    age =  int(input("Please enter your age: "))
    answer = checkinput("Are you a devops enthusiast? (yes/no): ")
    print(Day2(name, age, answer))