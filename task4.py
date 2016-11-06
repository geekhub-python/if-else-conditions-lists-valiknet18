#!/usr/bin/env python3

listOfNumbers = input()
listOfNumbers = [int(i) for i in listOfNumbers.split(" ")]
equals = 0

for i in range(len(listOfNumbers)):
    for j in range(i + 1, len(listOfNumbers)):
        if listOfNumbers[i] == listOfNumbers[j]:
            equals += 1

print(equals)
