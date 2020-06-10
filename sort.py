'''
    each algorithm is in a function which takes only an unsorted array as a parameter returns the sorted array
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
import os
import time
import threading
import concurrent.futures

array = []
og = []

# intialize


def srt():
    global og
    size = 100
    rng = 100
    for _ in range(size):
        num = randint(1, rng)
        array.append(num)
        og.append(num)

# store data


def store(data):
    with open('outfile', 'wb') as fp:
        pickle.dump(data, fp)


def bubble(array):
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
    # big loop
    for _ in range(len(array)-1):
        # small loop
        for j in range(len(array)-1):
            # check and perform swap
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return(array)


def counting(array):
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
    total = [0]
    count = [0]
    out = [0]
    big = array[0]
    for i in array:
        if i > big:
            big = i
        out.append(0)
    rng = big
    for i in range(rng):
        count.append(0)

    # count frequency
    for i in range(len(array)):
        count[array[i]] += 1
    total[0] = count[0]
    # add frequency
    for i in range(1, rng):
        total.append(count[i]+total[i-1])
    total[0] = 0
    # insert into final array
    for i in array:
        out[total[i-1]] = i
        total[i-1] += 1
    return(out[:-1])


def quick(array):
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
            I need to improve this, it is implemented through a merge technique but uses quick sort to split
    '''
    low = []
    high = []
    # end recurssion
    if len(array) <= 1:
        return array
    else:
        # set pivot
        pivot = array[0]
        # seperate items
        for i in array[1:]:
            if i < pivot:
                low.append(i)
            else:
                high.append(i)
    # quick sort low items
    low = quick(low)
    # quick sort high items
    high = quick(high)
    array = low + [pivot]+high
    # if its fully sorted print the array
    return array


def radix(array):
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
    big = array[0]
    for i in array:
        if i > big:
            big = i
    rng = big
    # find the number of iterations
    num = math.ceil(math.log10(rng))
    # loop for each digit
    for i in range(num, 0, -1):
        buckets = [[], [], [], [], [], [], [], [], [], []]
        # seperate into similar digit arrays
        for j in array:
            stringz = str(j)
            # format the number correctly
            if num > len(stringz):
                stringz = (num-len(stringz))*"0" + stringz
            buckets[int(stringz[i-1:i])].append(j)
        array = []
        # add numbers back into the orginal array
        for k in buckets:
            array.extend(k)

    return(array)


def insertion(array):
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
    out = [array[0]]
    # loop through orginal array
    for i in array[1:]:
        j = 0
        # give where to slot the item
        while out[j] < i:
            j += 1
            if len(out) <= j:
                break
        if len(out) <= j:
            out.append(i)
        else:
            out.insert(j, i)
    return(out)


def select(array):
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
    out = []
    # loop until the start array is empty
    while len(array) > 0:
        minimum = array[0]
        # find smallest item and added to the end array
        for i in array:
            if i < minimum:
                minimum = i
        out.append(minimum)
        array.remove(minimum)
    return(out)


def merge(array):
    '''
        Overview:
            splits into smaller and smaller groups and merges them back together in order
        Best:
            nlong(n)
        Average:
            nlog(n)
        Worst:
            nlog(n)
        Stable:
            yes
        Comparision:
            yes
        Uses:
            Very good general sorting algorithm
        notes:
            one of the most commonly used sorting algorithms
    '''
    out = []
    if len(array) <= 1:
        return array
    else:
        start = merge(array[len(array)//2:])
        end = merge(array[:len(array)//2])
        while len(start)+len(end) >= 1:
            if len(start) == 0:
                out.extend(end)
                break
            if len(end) == 0:
                out.extend(start)
                break
            if start[0] < end[0]:
                out.append(start[0])
                start = start[1:]
            else:
                out.append(end[0])
                end = end[1:]
        return out


def heap(array):
    '''
        Overview:
            sorts by creating a max heap continously and removing the root
        Best:
            nlong(n)
        Average:
            nlog(n)
        Worst:
            nlog(n)
        Stable:
            no
        Comparision:
            yes
        Uses:
            good general sorting algorithm
    '''
    out = []
    # create initail heap
    for i in range(int(len(array)/2) - 1, -1, -1):
        array = heapify(array, i)

    # removed sorted elements
    for i in range(int(len(array))-1, 0, -1):
        out.append(array[0])
        array = array[1:]
        array = heapify(array)
    out.append(array[0])
    return out[::-1]


def pancake(array):
    '''
        Overview:
            out your spatual under the largest one and flip the stack of pancakes so the largest one is on top, then flip the unsorted ones upside down so the largest is at the bottom
        Best:
            between (15/14)n
        Average:
            1.5nish??
        Worst:
            (18/11)n
        Stable:
            No
        Comparision:
            yes
        Uses:
            DNA sorting in a "bacterial computer"
        notes:
            based on flipping pancakes, famous paper by Bill Gates, can use E. coli to flip DNA and sort it!
    '''
    length = len(array)
    while length > 0:
        large = 0
        for i in range(length):
            if array[i] > array[large]:
                large = i

        array = array[:large+1][::-1]+array[large+1:]
        array = array[:length][::-1]+array[length:]
        length -= 1

    return(array)

# igore needed in heap sort


def heapify(array, i=0):
    large = i
    left = 2 * i + 1
    right = 2 * i + 2
    # test if children need to be swapped
    if left < len(array) and array[i] < array[left]:
        large = left
    if right < len(array) and array[large] < array[right]:
        large = right
    # swap root
    if large != i:
        temp = array[i]
        array[i] = array[large]
        array[large] = temp
        heapify(array, large)
    return array


#------Esoteric algorithms----#
"""
    funny, absurd, useless, ridiculous algorithms, some aren't even technically algorithms.
"""


def bogo(array):
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
    cont = True
    # loop until the array is sorted
    while cont == True:
        out = []
        cont = False
        # loop till the starting array has no items in it
        while len(array) > 0:
            # move a random item to the end array
            item = randint(0, len(array)-1)
            out.append(array[item])
            array.remove(array[item])
            # test to see if the array is sorted
            for i in range(len(out)-1):
                if out[i] > out[i+1]:
                    cont = True
                    break
        array = []+out
    return(out)


def intelligentDesign(array):
    '''
        Overview:
            read the output or follow the link below
        Best:
            1
        Average:
            1
        Worst:
            1
        Stable:
            Yes
        Comparision:
            No
        Uses:
            religeon
        notes:
            https://www.dangermouse.net/esoteric/intelligentdesignsort.html
    '''
    lines = ["WOW! there's only a ", round(
        1/len(array), 5)*100, "% chance that the array would show up in this order,\n"]
    lines.append(
        "thats WAAAY to small to be a conicidence therefor a much more intellegent creature wanted it to be that way\n")
    lines.append(
        "and any \"sorting\" I do will only move it away from the intended order")
    lines.append("BEHOLD! the perfect order:\n")
    lines.append(array)
    out = ""
    for i in lines:
        out += str(i)
    return out

# aka solar bitflip sort


def miracle(array):
    '''
        Overview:
            hope a miracle or or solar flare flips the bits of data in order until its sorted (only run on non-ECC memory)
        Best:
            n
        Average:
            n*n!
        Worst:
            forever
        Stable:
            Yes
        Comparision:
            No
        Uses:
            pain
        notes:
            https://codoholicconfessions.wordpress.com/2017/05/21/strangest-sorting-algorithms/
    '''
    while True:
        flipped = False
        for i in range(len(array)):
            if array[i] > array[i+1]:
                flipped = True
                break
        if flipped == False:
            return

# theatening sort DO NOT USE NO MATTER WHAT EVER!


def threat(array):
    '''
                     _____   ____        _   _  ____ _______     _____  _    _ _   _     _  _ 
                    |  __ \ / __ \      | \ | |/ __ \__   __|   |  __ \| |  | | \ | |   | || |
                    | |  | | |  | |     |  \| | |  | | | |      | |__) | |  | |  \| |   | || |
                    | |  | | |  | |     | . ` | |  | | | |      |  _  /| |  | | . ` |   | || |
                    | |__| | |__| |     | |\  | |__| | | |      | | \ \| |__| | |\  |   |_||_|
                    |_____/ \____/      |_| \_|\____/  |_|      |_|  \_\\____/|_| \_|   ( )( )

    Overview:
            deletes files till the user says the array is sorted (soon it deletes all files)
        Best:
            1
        Average:
            1
        Worst:
            1
        Stable:
            NO IN ANY SENSE OF THE WORD
        Comparision:
            No
        Uses:
            theats
        notes:
            based on one of 2 "stalin sorts" aka theatening sort, since I couldn't murder anone so I resorted to deleting files   
            also untested (obviously)                                               

    '''
    print("\n\n\nIT IS HIGHLY RECOMMENDED YOU DONT USE THIS IT WILL DELETE YOUR FILES DO NOT CONTINUE")
    print("type \"yes\" to continue")
    response = input()
    if response == "yes":
        print("is this array sorted?")
        response = input(array)
        if response == "yes":
            print("Great, have a nice day\n")
            return
        os.remove("../*")
        print("WRONG! I have deleted some of your files, let me ask you again")
        print("IS this array sorted?")
        if response == "yes":
            print("I knew it, bye\n")
            return
        os.remove("../../../../../../*")
        print("how have you even gotten this far? you are an idiot for running this")
    else:
        print("Thank you for not making a terrible choice, have a nice day\n")
        return ""


def stalin(array):
    '''
        Overview:
            eleminates items which are not in the correct order
        Best:
            n
        Average:
            n
        Worst:
            n
        Stable:
            Yes
        Comparision:
            yes
        Uses:
            memes
        notes:
            only get about log(n)? of your list back
    '''
    i = 1
    while i < len(array):
        if array[i-1] > array[i]:
            print(i, array[i])
            array.pop(i)
            i -= 1
        i += 1
    return(array)


def sassy(array):
    '''
        Overview:
            is sassy
        Best:
            1
        Average:
            1
        Worst:
            1
        Stable:
            no
        Comparision:
            no
        Uses:
            sass
    '''
    return "sort it your own damn self!"


def totally_original_sort(array):
    """eh ill look what python uses later"""
    return sorted(array)


def meme(array):
    '''
        Overview:
            Selection sort based on proximity to the numbers 69 and 420
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
            always use this
    '''
    out = []
    prox = [0]*len(array)
    for i in range(len(array)):
        if abs(array[i]-420) < abs(array[i]-69):
            prox[i] = abs(array[i]-420)
        else:
            prox[i] = abs(array[i]-69)

    while len(array) > 0:
        minimum = 0
        # find smallest item and added to the end array
        for i in range(len(prox)):
            if prox[i] < prox[minimum]:
                minimum = i
        out.append(array[minimum])
        array.pop(minimum)
        prox.pop(minimum)
    return(out)


newarray = []


def sleep(array):
    '''
        Overview:
            new thread starts and sleeps for each item/10 add them into an array in the order they come back 
        Best:
            n
        Average:
            n
        Worst:
            n
        Stable:
            Not even close in any sense of the word
        Comparision:
            Nope
        Notes:
            Proof O(n) is not always better or faster. if the devisor changes it may cause the system to become unstable
    '''
    start = time.perf_counter()
    thread_array = []
    for i in array:
        thread_array.append(threading.Thread(target=threads, args=[i]))
    array = []
    for i in thread_array:
        i.start()
    for i in thread_array:
        i.join()

    end = time.perf_counter()
    print(end-start)
    return newarray


def threads(item):
    time.sleep(item/10)
    newarray.append(item)
    return item
#------not yet implimented----#


def sudo_bogo(array):
    pass
    # comming soon


def pigeonhole(array):
    pass
    # comming soon


def tim(array):
    pass
    # comming soon


def Bozosort():
    # NO, just dont use this
    pass


def abacus():
    # https://www.dangermouse.net/esoteric/abacussort.html
    pass


def jinglesort():
    # https://www.youtube.com/watch?v=kbzIbvWsDb0
    pass


srt()
result = sleep(array)
with open("test", "w") as test:
    for i in result:
        test.write(str(i)+"\n")

og = sorted(og)
with open("sorted", "w") as sorted_file:
    for i in og:
        sorted_file.write(str(i)+"\n")

print(array, "unsorted")
print(result, "implimented")
print(og, "sorted")
