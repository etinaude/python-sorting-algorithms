from random import seed
from random import random
from random import randint
import sys
import pickle
import math

array = []
size = 100
count =[0]
out =[0]
rng = 100

#intialize
def srt():
    global size, array, rng, out, count
    for i in range(size):
        array.append(randint(1,rng))
    for i in range(rng):
        count.append(0)
        out.append(0)

#store data
def store(data):
    with open('outfile', 'wb') as fp:
        pickle.dump(data, fp)

#bubble sort
def bubble():
    global size, array, rng, out, count
    for i in range(0, size-1):
        for j in range(0, size-1):
            if array[j] > array[j+1]:
             temp = array[j]
             array[j] = array[j+1]
             array[j+1] = temp
    print(array)

#counting sort
def counting():
    global size, array, rng, out, count
    total = [0]
    for i in range(size):
        count[array[i]] += 1
    total[0]=count[0]

    for i in range(1,rng+1):
        total.append(count[i]+total[i-1])
    total[0]=0

    for i in array:
        out[total[i-1]] = i
        total[i-1] += 1
    print(out[:-1])
    
#radix sort
def radix():
    pass
    #comming soon

#merge sort
def merge_sort():
    pass
    #comming soon

#quick sort
def quick():
    pass
    #comming soon

#insertion sort
def insertion():
    pass
    #comming soon

#bogo sort
def bogo():
    pass
    #comming soon

#pigeonhole sort
def pigeonhole():
    pass
    #comming soon

#tim sort
def tim():
    pass
    #comming soon

#heap sort
def heap():
    pass
    #comming soon

#pancake sort
def pancake():
    pass
    #comming soon


srt()
print(array)
print()
bubble()
