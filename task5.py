#!/env/bin/python3

arrayOfNumbers = input("Write array of number in string: ")
arrayOfNumbers = arrayOfNumbers.split(' ')
arrayOfNumbers = [int(i) for i in arrayOfNumbers]

for i in range(len(arrayOfNumbers) - 1):
    if (arrayOfNumbers[i] > 0 and arrayOfNumbers[i + 1] < 0)  or (arrayOfNumbers[i] < 0 and arrayOfNumbers[i + 1] > 0):
        print(arrayOfNumbers[i], arrayOfNumbers[i + 1])
        break
