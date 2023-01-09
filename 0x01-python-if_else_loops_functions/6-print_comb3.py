#!/usr/bin/python3
i = 1
while i < 100:
    if i % 10 == 0:
        i = int(i + (i / 10) + 1)
        continue
    print("{:02d}".format(i), end=", " if i < 89 else "\n")
    i += 1
