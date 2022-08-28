import numpy as np
import matplotlib.pyplot as plt

def bubble_sort(li, x, delay):
    n = len(li)
    color = ['black'] * n
    for i in range(n):
        for j in range(0, n-i-1):
            color[j], color[j+1] = 'red', 'red'
            plt.bar(x, li, color=color)
            plt.pause(delay)
            plt.clf()
            color[j], color[j+1] = 'black', 'black'
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    plt.bar(x, li, color=color)
    plt.show()
            
    return li


def insertion_sort(li, x, delay):
    n = len(li)
    color = ['black'] * n
    for i in range(1, n):
        key_item = li[i]
        j = i - 1
        while j >= 0 and li[j] > key_item:
            color[j+1] = 'red'
            plt.bar(x, li, color=color)
            plt.pause(delay)
            plt.clf()
            li[j + 1] = li[j]
            color[j+1] = 'black'
            j -= 1

        li[j + 1] = key_item

    plt.bar(x, li, color=color)
    plt.show()

    return li
    