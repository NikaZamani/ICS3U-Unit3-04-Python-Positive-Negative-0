#!/usr/bin/env python3

# Created by: Nika Zamani
# Created on: April 2021
# This program will read an integer and display its sign

def main():
    # this function reads an integer and displays its sign

    # input
    integer = int(input("Enter an integer: "))

    # process & output
    if integer > 0:
        print(integer, "is a positive number. ")
    elif integer < 0:
        print(integer, "is a negative number. ")
    else:
        print(integer, "is just zero! ")

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
