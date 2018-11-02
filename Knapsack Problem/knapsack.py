from ast import literal_eval
from collections import namedtuple
from operator import attrgetter 

def weight_of_set(set):
    weight = 0
    for item in set:
        weight += item.weight
    return weight

def value_of_set(set):
    value = 0
    for item in set:
        value += item.value
    return value

def brute_force(items, knapSize):
    bestSac = []
    maxVal = 0
    currentSac = None
    for i in range(1, 1 << len(items)):
        bestSac.append([x for k, x in enumerate(items) if 1 << k & i])
    
    for set in bestSac:
        weight = weight_of_set(set)
        if weight > knapSize:
            continue
        value = value_of_set(set)
        if value > maxVal:
            maxVal = value
            currentSac = set
            
    print("The values obtained through a brute force algorithm totals", maxVal, "\n",sorted(currentSac, key=attrgetter('value')), "\n")
    
def greedy_ratio(items, knapSize):
    items_by_ratio = sorted(items, key=lambda x: x.weight/x.value)
    #print(items_by_ratio)
    weight = 0
    maxVal = 0
    currentSac = []
    for x in items_by_ratio:
        if knapSize - weight >= x.weight:
            currentSac.append(x)
            weight = weight + x.weight
            maxVal = maxVal + x.value
    print("The values obtained through a greedy method totals", maxVal, "\n", sorted(currentSac, key=attrgetter('value')), "\n")
            

def dynamic_programming(items, knapSize):
    table = [[0 for max in range(knapSize + 1)] for size in range(len(items) + 1)]
    for x in range(1, len(items) + 1):
        weight, value = items[x-1]
        for y in range(1, knapSize + 1):
            if weight > y:
                table[x][y] = table[x-1][y]
            else:
                table[x][y] = max(table[x-1][y],
                                  table[x-1][y-weight] + value)
    result = []
    wgt = knapSize
    for x in range(len(items), 0, -1):
        added = table[x][wgt] != table[x-1][wgt]
 
        if added:
            wt, val = items[x-1]
            result.append(items[x-1])
            wgt = wgt- wt
 
    print("The values obtained through a dynamic programming algo total" , value_of_set(result),"\n", sorted(result, key=attrgetter('value')))




Item = namedtuple('Item', ('weight', 'value'))
with open('input.txt', 'r') as f:
    knapSize = int(f.readline())
    weights = literal_eval('(' + f.readline()+')')
    values = literal_eval('(' + f.readline() +')')
items = list(map(lambda x: Item(*x), zip(weights, values)))
greedy_ratio(items, knapSize)
brute_force(items, knapSize)
dynamic_programming(items, knapSize)
    
    
    