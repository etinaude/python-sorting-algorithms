array = [6,5,4,3,7,5,3,2,1,6,0,9]
count = [0,0,0,0,0,0,0,0,0,0,0,0]
out =   [0,0,0,0,0,0,0,0,0,0,0,0]
nums =  [0,1,2,3,4,5,6,7,8,9]
def bubble(array,size):
    for i in range(0, size):
        for j in range(0, size):
            if array[j] > array[j+1]:
             temp = array[j]
             array[j] = array[j+1]
             array[j+1] = temp
    print(array)
def counting(array,size,rng):
    for i in range(0,size):
        count[array[i]] += 1
    count[0] += -1
    print(count)
    for i in range(1,rng):
        count[i] = count[i-1] + count[i]
    count[0] = 0
    for i in range(rng-1,1,-1):
        count[i] = count[i-1]
    for i in range(0,size):
        out[count[array[i]]] = array[i]
        count[array[i]] += 1
    print(out)
counting(array,12,12)
bubble(array,11)