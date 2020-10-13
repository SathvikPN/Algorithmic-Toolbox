# python3
'''
Problem Statement:
Maximum Pairwise Product Problem
Find the maximum product of two distinct numbers in a sequence of non-negative integers
Input: A sequence of non-negative
integers.
Output: The maximum value that
can be obtained by multiplying
two different elements from the sequence.
Constraints. 2 ≤ n ≤ 2 · 105; 0 ≤ a1,...,an ≤ 2 · 105.
'''


import random
import time

#Naive approach - Iterating every possible combination
def max_pairwise_product1(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        if(n<2):
            max_product = numbers[0]
            break
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

#Faster Approach - multiply only for biggest and 2nd biggest number in list
def max_pairwise_product2(numbers):
    n = len(numbers)
    biggest1,biggest2 = 0,0
    for i in range(n):
        if numbers[i]>biggest1:
            index = i
            biggest1 = numbers[i]
    for j in range(n):
        if (n<2):
            print("Two elements didn't exist to multiply",end=' ')
            biggest2=1
            break
        if ((j!=index)and(numbers[j]>biggest2)):
            biggest2 = numbers[j]

    max_product = (biggest1*biggest2)
    return max_product

def stressTest(N,M):
    while True:
        n = random.randint(1,N)
        A=[]
        for i in range (1,n+1):
            x = random.randint(0,M)
            A.append(x)
        print('Random Input Numbers list=',A)
        result1 = max_pairwise_product1(A)
        result2 = max_pairwise_product2(A)
        if result1==result2:
            print("Result=OK")
            time.sleep(0.5)
        else:
            print("Wrong. Result Mismatch",result1,result2)
            return
    


  
if __name__ == '__main__':
    #input_n = int(input())
    print("max_pairwise_product")
    input_numbers = [int(x) for x in input("sequence: ").split()]
    print(max_pairwise_product2(input_numbers))

    

    print(f'''
Stress Testing...
Enter max list size and max list values''')
    N,M = input().split()
    stressTest(int(N),int(M))
   
