import ast
import math
from time import perf_counter
from math import hypot, floor, pow, sqrt

def bruteForce(points):
    length = len(points)
    min = -1
    for x in range(len(points)):
        for y in range(1, len(points)):
            if x != y:
                this = hypot((points[x][0] - points[y][0]), (points[x][1] - points[y][1]))
                if min == -1:
                    min = this
                else:
                    if min > this:
                        min = this
    return min
                    
def calculateTime( time ):    #method to compute how much time a method takes to the 8th decimal place
        print("Time to compute GCD using above method: %.8f" %time, "s \n")               
            
            
        


def EfficientClosestPair(p,q):
    length= len(p)
    if length < 3:
         return bruteForce(p)
    pr = p[length // 2:] # 1
    qr = sorted(pr, key=lambda x: x[1])
    pl = p[:length // 2 + 1]
    ql = sorted(pl, key=lambda x: x[1])
    
    
    dl = EfficientClosestPair(pl,ql)
    dr = EfficientClosestPair(pr,qr)
    d = min(dl, dr)
    m = p[(length//2) -1][0]
    s = [x for x in q if abs(x[0] - m) < d]
    dsq = pow(d,2)
    for x in range(len(s)-2):
        k= x+1
        while k < (len(s)) and (pow((s[k][1] - s[x][1]), 2) < dsq):
            dsq = min(pow((s[k][0]-s[x][0]),2) + pow((s[k][1] - s[x][1]),2), dsq)
            k = k+1
    return sqrt(dsq)
        

   
with open('input.txt', 'r') as f:
    points = ast.literal_eval(f.read())

if len(points) < 2:
    print("Not enought coordinates in input file or formatting incorrect. Exiting")
    exit(0)
        
p = sorted(points, key=lambda x: x[0])
q = sorted(points, key=lambda x: x[1])


start=perf_counter()      #starts clock timer
shortest = bruteForce(points)
end= perf_counter()       #stops timer
print("The shortest distace using brute force is ", shortest)
calculateTime(end-start)

start=perf_counter()
shortest = EfficientClosestPair(p,q)
end= perf_counter()       #stops timer
print("The shortest distace using Divide and Conquer is ", shortest)
calculateTime(end-start)


