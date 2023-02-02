# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 17:55:26 2022

@author: 253364
"""

import matplotlib.pyplot as plt
import pandas as pd
import os


def clean(lis):
    for i in range(len(lis)):
        if lis[i] == 0:
            lis[i] = lis[i-1]
        else:
            pass
        
    return lis


amount_of_data = len(os.listdir("results_logs\\"))
data = pd.read_csv("results_logs\\log_entry_{}.csv".format(amount_of_data - 1))

print(data)

x = data['bird1_x']
y = data['bird1_y']

xs = clean(x)
ys = clean(y)

plt.plot(xs, ys)

x = data['bird2_x']
y = data['bird2_y']

xs = clean(x)
ys = clean(y)

plt.plot(xs, ys)


x = data['bird3_x']
y = data['bird3_y']

xs = clean(x)
ys = clean(y)

plt.plot(xs, ys)


x = data['bird4_x']
y = data['bird4_y']

xs = clean(x)
ys = clean(y)


plt.title("Movement of birds")
plt.plot(xs, ys)
plt.xlabel("X coordinates")
plt.ylabel("Y coordindates")
plt.show()


for k, d in data.items():
    print(k)