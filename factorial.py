#!/usr/bin/env python3

# Created By: Peter Sobowale
# Date: November 3, 2022
# This program allows the user to enter a
# whole number. It then uses a do..while
# loop to calculate the factorial of that number.
import math


def main():
    # initialize the loop counter and sum
    loop_counter = 0
    fact_ans = 1

    # get the user number as a string
    user_num_string = input("Enter a positive integer: ")
    print("")

    # try catch for erroneous data
    try:
        # set user_num = int(user_num_string)
        user_num = int(user_num_string)

        # if statement for if user_num is a negative
        if user_num > 0:

            # calculate the sum of all numbers from 0 to user number
            while True:
                loop_counter = loop_counter + 1
                fact_ans = fact_ans * loop_counter
                print("Tracking {} time(s) through loop.".format(loop_counter))
                if loop_counter >= user_num:
                    break

            # display the factorial of the user input
            print("{}! = {}".format(user_num, fact_ans))

        # else if user_num is 0
        elif user_num == 0:
            print("0! = 1")
        elif user_num < 0:
            print("{} is not a positive integer.".format(user_num_string))

    # exception for strings and floats
    except ValueError:
        print("{} is not a positive integer.".format(user_num_string))

    # display ending message
    finally:
        print("\nThanks for playing!")


if __name__ == "__main__":
    main()
