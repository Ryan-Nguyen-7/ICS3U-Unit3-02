#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on November 2020
# This program checks if there are over 30 students


import constants


def main():
    # this function checks if there is over 30 students
    
    # input
    number_of_students = int(input("Enter the number of students: "))
    print("")

    # process
    if number_of_students > constants.MAX_STUDENT_NUMBER:
        # output
        print("Too many students!")
        
if __name__ == "__main__":
    main()
