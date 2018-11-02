#Kamil Gumeinny
#kmgumienny
#168063623

from time import perf_counter #this will be used for calculating time

def getArgument( str ):
    counter = 0 #counter keeps track of illegal inputs
    
    while (counter < 3):
        try:                                           #tries getting user input and converting to integer
            print("What is the ", str, " integer? ")
            number = int(input())
        except ValueError:                             #if user inputs illegal value, the exception is caught and the counter is increased
            print("Please enter an integer!")
            counter += 1
            continue
        
        if number > 0:
            return number
        else:
            print("Not a valid integer.")
            counter += 1
    
    if counter == 3:                                   #program quits when counter reaches 3 by returning negative -1,
        print("Too many invalid inputs. Goodbye.")     #which is evaluated in checkExit method
        return -1

def checkExit( argValue ):  #method to check if program should quit
    if argValue == -1:
        exit(1)

def euclidean(arg1, arg2): #the euclidean algorithm
    m = arg1               #the drawbacks of pass by value
    n = arg2
    r = 0
    while n != 0:
        r = m%n
        m = n
        n = r
    return m

def integerChecking(arg1, arg2):  #the Consecutive Integer Checking
    m = arg1
    n = arg2
    t = min(m,n)
    
    while 1:
        x = m % t
        if not x:
            x = n % t
            if not x:
                return t
        t -= 1

def getPrimes( num ):   #computes an array of primes for Middle School Method for each of the 2 numbers
    listPrimes = []
    d = 2
    while (d*d) <= num: #discrete math-> check every number less than sqrt(n)
        while (num % d) == 0:
            num = num // d  #prevents float
            listPrimes.append(d)
        d += 1
    if num > 1:
       listPrimes.append(num)
    return listPrimes


def midSchool(arg1,arg2):        #the Middle School Method
    m = arg1
    n = arg2
    
    primesm = getPrimes(m)
    primesn = getPrimes(n)
    gcd = 1                     #variable to hold gcd for Middle School Method
    
    if(m > n):
        for m in primesm:
            for n in primesn:
                if n == m:                     #when two of the same numbers are found, they are multiplied into gcd  
                    gcd *= n                   #variable and are then removed from the inner loop, reducing computation and
                    primesn.remove(n)          #avoiding duplication
        return gcd
    else:
        for n in primesn:
            for m in primesm:
                if n == m:                     #when two of the same numbers are found, they are multiplied into gcd  
                    gcd *= n                   #variable and are then removed from the inner loop, reducing computation and
                    primesm.remove(m)          #avoiding duplication
        return gcd

def calculateTime( time ):    #method to compute how much time a method takes to the 8th decimal place
        print("Time to compute GCD using above method: %.8f" %time, "s \n")
    
        
#the beginning of the main code
        
        
m = getArgument("first")   #get value of first integer
checkExit(m)               #check to see if method did not return exit value 
n = getArgument("second")
checkExit(n)

answer = 0

start=perf_counter()      #starts clock timer
answer = euclidean(m,n)   #finds GCD using method
end= perf_counter()       #stops timer

print("Using Euclidean's Algorithm, the GCD is ", answer)   #print result 
calculateTime(end-start)                                    #print time

start=perf_counter()
answer = integerChecking(m,n)
end= perf_counter()

print("Using Consecutive Integer Checking, the GCD is ", answer)
calculateTime(end-start)


start=perf_counter()
answer = midSchool(m,n)
end= perf_counter()

print("Using Middle School Method, the GCD is ", answer)
calculateTime(end-start)







    

              