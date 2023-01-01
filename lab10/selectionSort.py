#  Simple implementation of Selection Sort in Python
from random import randint

def selectionSort(values):
    """Takes a list as input, sorts it using
    selection sort, and returns sorted list"""

    # First compute length of list
    size = len(values)

    # Traverse through all list elements
    for i in range(size):

        # Find the index of the minimum element in i + 1 onwards
        minIndex = i
        for j in range(i + 1, size):
            if values[minIndex] > values[j]:
                minIndex = j

        # Swap the found min element with ith element
        values[i], values[minIndex] = values[minIndex], values[i]

    return values

if __name__ == "__main__":
    size = 10
    randList = []

    # Populate list with random numbers
    for _ in range(size):
        randList.append(randint(0, 100))

    # Print unsorted list
    print("List before sorting:")
    print(randList)

    # Call selection sort function
    sortedList = selectionSort(randList)

    # Print sorted list
    print("Sorted list:")
    print(sortedList)
