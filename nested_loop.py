#!/usr/bin/env python3

# created by: Youngjun Kim
# created on: May 2021
# This program using nested loop

def main():
    # this function using nested loop
    counter1 = 0
    counter2 = 0
    counter3 = 0
    for counter1 in range(256):
        for counter2 in range(256):
            for counter3 in range(256):
                print("RGB({0},{1},{2})".format(counter1, counter2, counter3))


if __name__ == "__main__":
    main()
