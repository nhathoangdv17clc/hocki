#!/usr/bin/python3.6

import algorithms 
import copy

if __name__ == "__main__":
    arr1 = [-4,1,3,1,4,5,2,4,6,2,234,23,4,2341,23,213]
    print("Before:\n{0}\n".format(arr1))

    select = input("Which algorithm you want to use?\n1:quick sort\n2:selection sort\nyour selection: ")

    if select == '1':
        algorithms.quickSort(arr1, 0, len(arr1) - 1)
        print("\nAfter:\n{0}\n".format(arr1))
    elif select == '2':
        arr1 = algorithms.selectionSort(arr1)
        print("\nAfter:\n{0}\n".format(arr1))
    else:
        print("Your selection is not correct, try again!\n")
        
