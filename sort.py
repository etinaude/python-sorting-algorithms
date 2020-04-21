'''
    each algorith is in a function which prints a sorted array (ill change it to return)
    there are notes before each algorithm explaining it

    n = number of elements to sort
    d = number of digits in the largest element
    r = range of elements (largest - smallest)
    k = size of key

    the best, average and worst shows the trend of how each algorith will perform when increasing these values.

    I will continue improving this and adding new algorithms
'''

from random import seed
from random import random
from random import randint
import sys
import pickle
import math

array = []
size = 10
count =[0]
out =[0]
rng = 10
og=[]

#intialize
def srt():
    global size, array, rng, out, count, og
    for i in range(size):
        num = randint(1,rng)
        array.append(num)
        og.append(num)
    for i in range(rng):
        count.append(0)
        out.append(0)

#store data
def store(data):
    with open('outfile', 'wb') as fp:
        pickle.dump(data, fp)



#bubble sort
def bubble():
    '''
        Overview:
            swap conscutive numbers until its sorted
        Best:
            n
        Average:
            n^2
        Worst:
            n^2
        Stable:
            Yes
        Comparision:
            Yes
        Uses:
            Don't use it unless you are teaching the basics of sorting
    '''
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
    '''
        Overview:
            count the numbers of items places before the place of each item
        Best:
            n+r
        Average:
            n+r
        Worst:
            n+r
        Stable:
            Yes
        Comparision:
            No
        Uses:
            Very good sort for integers, esspcailly if the data set has a small range
    '''
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
    '''
        Overview:
            Pivot items around 
        Best:
            n*log(n)
        Average:
            n*log(n)
        Worst:
            n^2
        Stable:
            no
        Comparision:
            yes
        Uses:
            good general algorithm, slower than merge sort on average but uses less space (usually)
        Notes: 
            I need to improve this
    '''
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
    '''
        Overview:
            Sort based on each digit of an integer
        Best:
            n*(k/d)
        Average:
            n*(k/d)
        Worst:
            n*(k/d)
        Stable:
            Yes
        Comparision:
            No
        Uses:
            Very good sort for integers, esspcailly if the numbers have few digits
        Notes: 
            this is a LSD radix I might add a MSD later 
    '''
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

#insertion sort
def insertion():
    '''
        Overview:
            Insert each number into its correct place
        Best:
            n
        Average:
            n^2
        Worst:
            n^2
        Stable:
            Yes
        Comparision:
            yes
        Uses:
            not great, easy to code use block sort instead if you need it to be stable and are short on memory
    '''
    global array
    out =[array[0]]
    #loop through orginal array
    for i in array[1:]:
        j = 0
        #give where to slot the item
        while out[j] < i:
            j+=1
            if len(out) <= j:
                break
        if len(out) <= j:
            out.append(i)
        else:
            out.insert(j,i)
    print(out)

#selection sort
def select():
    '''
        Overview:
            Select the smallest item one by one
        Best:
            n^2
        Average:
            n^2
        Worst:
            n^2
        Stable:
            No
        Comparision:
            Yes
        Uses:
            Don't, its similar to insertion sort but worse since best is worse and its not stable
    '''
    global array
    out =[]
    #loop until the start array is empty
    while len(array)>0:
        minimum = array[0]
        #find smallest item and added to the end array
        for i in array:
            if i < minimum:
                minimum = i
        out.append(minimum)
        array.remove(minimum)
    print(out)

#bogo sort
def bogo():
    '''
        Overview:
            Pick random orders in the hope that one will work
        Best:
            n
        Average:
            n*n!
        Worst:
            FOREVER!!!
        Stable:
            No
        Comparision:
            kinda of
        Uses:
            MEMES!, its closer to shuffling than a good sorting algoritm
        notes:
            It can go on forever so dont use it unless you are trying to show what not to do
    '''
    # WARNING this can take a LONG time only run with fewer than 10 items to sort
    global array
    cont =True 
    #loop until the array is sorted
    while cont == True:
        out =[]
        cont = False
        #loop till the starting array has no items in it
        while len(array) > 0:
            #move a random item to the end array
            item = randint(0,len(array)-1)
            out.append(array[item])
            array.remove(array[item])
            #test to see if the array is sorted
            for i in range(len(out)-1):
                if out[i] > out[i+1]:
                    cont = True
                    break
        array = []+out
    
    print(out)
    
    
#sudo bogo sort
def sudo_bogo():
    pass
    #comming soon

#merge sort
def merge_sort():
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
print(array, "unsorted")
print()
merge_sort()
print(sorted(og), "sorted")
