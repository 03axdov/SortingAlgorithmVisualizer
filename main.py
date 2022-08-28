from sorting_algorithms import *
import numpy as np

def main():
    while True:
        try:
            length = int(input("Select the list length: "))
            if length <= 0:
                print('')
                print("ERROR: Length must be 1 or longer")
                print('')
                continue
            break
        except (ValueError, Exception):
            print("")
            print("ERROR: Length must be an integer")
            print("")

    while True:
        try:
            max = int(input("Select the highest possible number in the list: "))
            break
        except ValueError:
            print("")
            print("ERROR: Max must be an integer")
            print("")

    while True:
        try:
            delay = float(input("Specify the delay between calculation (0.01 <= delay): "))
            break
        except ValueError:
            print("")
            print("ERROR: Delay must be a float")
            print("")
        
    li = np.random.randint(0, max + 1, length)
    x = np.arange(0, length, 1)

    algorithms = {'1': ['Bubble Sort', bubble_sort]}
    print('')
    print("Sorting algorithms: ")
    for key, values in algorithms.items():
        print(f"{key} - {values[0]}")
    while True:
        try:
            algorithm = algorithms[input("Specify an algorithm (Ex. Typing 1 refers to the Bubble Sort algorithm): ")]
            break
        except KeyError:
            print("")
            print("ERROR: Please enter a valid value")
            print("")

    algorithm[1](li, x, delay)
    



if __name__ == '__main__':
    main()