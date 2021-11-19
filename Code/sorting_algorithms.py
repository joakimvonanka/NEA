test1 = [7, 6, 5, 9, 8, 4, 3, 1, 2, 0]
test2 = ["anton", "david", "mohammed", "alex"]

#Gnome Sort - O(n^2)
def GnomeSort(x):
    i, j, size = 1, 2, len(x)
    while i < size:
        if x[i - 1] <= x[i]:
            i, j = j, j+1
        else:
            x[i - 1], x[i] = x[i], x[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    print(x)
"""
GnomeSort(test1)
print(test1)
"""

#Cocktail Sort - O(n^2)
def CocktailSort(x):
    up = range(len(x)-1)
    while True:
        for indices in (up, reversed(up)):
            swapped = False
            for i in indices:
                if x[i] > x[i + 1]:
                    x[i], x[i + 1] = x[i + 1], x[i]
                    swapped = True
            if not swapped:
                return
""""
CocktailSort(test1)
print(test1)
"""

#Bogosort - EXTREMELY Inefficient, just for fun. - O(n!)
import random
def bogosort(first):
    random.shuffle(first)
    while first != sorted(first):
        random.shuffle(first)
    return first
"""
bogosort(test1)
print(test1)
"""

#Bubble Sort - O(n^2)
def bubblesort(list):
    swapped = True
    iteration_no = 0
    while (swapped):
        swapped = False
        for i in range(len(list) - iteration_no - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                swapped = True
        iteration_no += 1
"""
bubblesort(test1)
print(test1)
"""

#Radix Sort
def radix():
    def countingSortForRadix(inputArray, placeValue):
        countArray = [0] * 10
        inputSize = len(inputArray)
        for i in range(inputSize): 
            placeElement = (inputArray[i] // placeValue) % 10
            countArray[placeElement] += 1
        for i in range(1, 10):
            countArray[i] += countArray[i-1]
        outputArray = [0] * inputSize
        i = inputSize - 1
        while i >= 0:
            currentEl = inputArray[i]
            placeElement = (inputArray[i] // placeValue) % 10
            countArray[placeElement] -= 1
            newPosition = countArray[placeElement]
            outputArray[newPosition] = currentEl
            i -= 1
            
        return outputArray

    def radixSort(inputArray):
        maxEl = max(inputArray)
        D = 1
        while maxEl > 0:
            maxEl /= 10
            D += 1
        placeVal = 1
        outputArray = inputArray
        while D > 0:
            outputArray = countingSortForRadix(outputArray, placeVal)
            placeVal *= 10  
            D -= 1
        return outputArray

    sorted = radixSort(test2)
    print(sorted)
"""
radix()
"""