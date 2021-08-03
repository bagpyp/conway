import random as r
from pprint import pprint
from time import sleep
import os

n = 15
m = 15

# initialize array
arr = [[0 for i in range(m+2)] for i in range(n+2)]
for i in range(1,n+1):
    for j in range(1,m+1):
        arr[i][j] = r.randint(0,1)

pprint(arr)
def neighb_i(i,j):
    """
    returns a list of adddress of a neighbor
    restricted from edge cases 
    0,0 -> 1,0 1,1 0,1   
    """
    neighbis = []
    for x in range(-1,2):
        for y in range(-1,2):
            neighbis.append((i+x, j+y))
    neighbis.pop(4)
    return neighbis

def neighbs(arr, i, j):
    total = 0
    for x,y in neighb_i(i,j):
        total += arr[x][y]
    return total

print(neighbs(arr, 3,4))

def new_arr(arr):
    arr_2 = arr
    for i in range(1,n+1):
        for j in range(1,m+1):
            if arr_2[i][j]==1:
                if neighbs(arr,i,j) < 2:
                    arr_2[i][j] = 0
                elif neighbs(arr,i,j) in [2,3]:
                    pass
                elif neighbs(arr,i,j) > 3:
                    arr_2[i][j] = 0
            else:
                if neighbs(arr,i,j)==3:
                    arr_2[i][j]=1
    return arr_2

while True:
    os.system('clear')
    pprint(arr)
    arr = new_arr(arr)
    sleep(.2)
