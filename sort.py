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
rng = 101

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
    #big loop
    for i in range(0, size-1):
        #small loop
        for j in range(0, size-1):
            #check and perform swap
            if array[j] > array[j+1]:
             temp = array[j]
             array[j] = array[j+1]
             array[j+1] = temp
    print(array)

#counting sort
def counting():
    global size, array, rng, out, count
    total = [0]
    #count frequency
    for i in range(size):
        count[array[i]] += 1
    total[0]=count[0]
    #add frequency
    for i in range(1,rng+1):
        total.append(count[i]+total[i-1])
    total[0]=0
    #insert into final array
    for i in array:
        out[total[i-1]] = i
        total[i-1] += 1
    print(out[:-1])
    
#quick sort
def quick(arrays,within = False):
    low = []
    high = []
    # end recurssion
    if len(arrays) <= 1:
        return arrays
    else:
        #set pivot
        pivot = arrays[0]
        #seperate items
        for i in arrays[1:]:
            if i<pivot:
                low.append(i)
            else:
                high.append(i)
    #quick sort low items
    low = quick(low, True)
    #quick sort high items
    high = quick(high,True)
    arrays = low + [pivot]+high
    #if its fully sorted print the array
    if within == False:
            print(arrays)
    return arrays

#radix sort
def radix():
    global array, rng
    #find the number of iterations
    num = math.ceil(math.log10(rng))
    #loop for each digit
    for i in range(num,0,-1):
        buckets =[[],[],[],[],[],[],[],[],[],[]]
        #seperate into similar digit arrays
        for j in array:
            stringz = str(j)
            #format the number correctly
            if num>len(stringz):
                stringz = (num-len(stringz))*"0" +stringz 
            buckets[int(stringz[i-1:i])].append(j)
        array = []
        #add numbers back into the orginal array
        for k in buckets:
            array.extend(k)
    
    print(array)

#merge sort
def merge_sort():
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
radix()
print(sorted(array))
