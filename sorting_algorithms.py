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