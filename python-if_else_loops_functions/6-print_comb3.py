#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i != j:
            print("{:0d}{:0d}".format(i, j), end=", " if i < 8 else "\n")
