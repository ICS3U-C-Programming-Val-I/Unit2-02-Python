#!/usr/bin/env python3

# Created By: Val Ijaola
# Date: September 26, 2023
# This program Calculates the area and perimeter of a rectangle with
# the inputed dimensions in cm.

import math


def main():
    # Input - Length & Width.
    # defining the variables "length" and "width."
    length = int(input("What is the length of the rectangle in cm? "))
    width = int(input("What is the width of the rectangle in cm? "))

    # process - Calculating length and width.
    area = length * width
    perimeter = 2 * (length + width)

    # output
    print("The area of the rectangle is {}cm^2".format(area))
    print("The perimeter of the rectangle is {}cm".format(perimeter))


if __name__ == "__main__":
    main()
