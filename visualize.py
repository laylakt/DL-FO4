import matplotlib.pyplot as plt
import numpy as np
import timeit
import math
import random


"""
def formula(n, p, q):
    f = []
    f[0] = p[0]
    for i in range(n):
        f[i+1] = f[i] & ([]*i (p[i] -> q[i]))

    return f


def visualize(f):

    plt.rcParams['figure.figsize'] = [10, 6]
    for i in range(len(f)):
        ns = np.linspace(i, 1000, len(f), dtype=int)
        ts = timeit.timeit('evaluate(f[i)', 'from __main__ import evaluate, f')
        plt.plot(ns, ts, 'bo')
    plt.show()
    
"""


