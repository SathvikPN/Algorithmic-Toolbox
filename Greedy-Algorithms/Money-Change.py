''' Money Change Question
Convert money into min no. of coins [Denominations 1,5,10 only]
'''
import time

n = int(input())
# starting time
start = time.time()

def minCoins(n):
    a = n//10
    b = (n%10)//5
    c = (n%10)%5
    print("{1} : Rs.{0} coins ".format(10,a))
    print("{1} : Rs.{0} coins ".format(5,b))
    print("{1} : Rs.{0} coins ".format(1,c))
    
    return a+b+c

print(minCoins(n))

# end time
end = time.time()
print(f"Runtime of the program is {end - start} seconds")
