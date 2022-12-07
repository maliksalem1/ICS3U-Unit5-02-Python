#!/usr/bin/env python3
# Created by: Kyanh Pham
# Created on: Nov 2022
# This program uses parameters and finds the area
#  of a triangle


def calculate_area_triangle(base, height):
    # calculate area

    # process
    area = (base * height) / 2

    # output
    print("\nThe area is {0} cm².".format(area))


def main():
    # this function calls other functions

    # input
    height_from_user = input("Enter the height of a triangle (cm): ")
    base_from_user = input("Enter the base length of a triangle (cm): ")

    try:
        height = int(height_from_user)
        base = int(base_from_user)
        calculate_area_triangle(base, height)
    except ValueError:
        print("\nInvalid Input")

    print("\nDone.")


if __name__ == "__main__":
    main()
