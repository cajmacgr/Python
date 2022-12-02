"""
By: Caleb MacGregor
"""
import numpy as np
import matplotlib.pyplot as plt
import simplerandom.iterators as sri

"""
Visualization of difference in random number generators
"""
def distribution_random():
    plt.clf
    x_vals = []
    y_vals = []
    seed = 0
    num = 10000
    np.random.seed(seed)
    for i in range(num):
        x_vals.append(np.random.randint(0, num))
        y_vals.append(i)
    plt.figure(0)
    plt.scatter(x_vals, y_vals, c = 'b', s=2)
    plt.title('Random')
    plt.savefig("distribution_random")
    pass

def distribution_KISS():
    plt.clf
    x_vals = []
    y_vals = []
    num = 10000
    rng_kiss = sri.KISS(123958, 34987243, 3495825239, 2398172431)
    for i in range(num):
        x_vals.append(next(rng_kiss) % num)
        y_vals.append(i)
    plt.figure(1)
    plt.scatter(x_vals, y_vals, c = 'b', s=2)
    plt.title('KISS')
    plt.savefig("distribution_KISS")   
    pass

def distribution_SHR3():
    plt.clf
    x_vals = []
    y_vals = []
    num = 10000
    rng_shr3 = sri.SHR3(3360276411)
    for i in range(num):
        x_vals.append(next(rng_shr3) % num)
        y_vals.append(i)
    plt.figure(2)
    plt.scatter(x_vals, y_vals, c = 'b', s=2)
    plt.title('SHR3')
    plt.savefig("distribution_SHR3")
    pass

########################################


    """"
    Only uncomment 1 function at a time
    """
if __name__ == '__main__':
    distribution_random()
    #distribution_KISS()
    #distribution_SHR3()