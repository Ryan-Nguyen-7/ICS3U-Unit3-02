#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on November 2020
# This program will ask the user to guess a number
#    and will tell them know if they are right


import constants


def main():
    # this function checks if the guess was right

    # input
    guess = int(input("Guess my number: "))
    print("")

    # process
    if guess == constants.MY_NUMBER:
        # output
        print("My number is 7!")


if __name__ == "__main__":
    main()
