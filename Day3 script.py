#!/usr/bin/env python3

"""
This is a day 3 script with List and Loops

We have also added in a new concept called list comprehension into this script

"""
def list_printer (tools: list, fav: str):
    for t in tools:
        if t.strip().lower() == fav:
            print(f"{t} is the one you love the most")
        else:
           print( f"{t}")

    f"Thanks for telling me your tools and the one you love the most :)"




if __name__ == "__main__":
    Seperator = input("Please enter the seperator to be used by your self to seperate you tools (Anything like , | etc): ").strip()
    List_of_tools = input("Now please use the seperator and give me the list of your tools: ")
    tools = [t.strip() for t in List_of_tools.split(Seperator)]
    Fav = input("Please enter name of your favourite tool: ").strip().lower()
    list_printer(tools,Fav)
