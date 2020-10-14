#Last digit of Nth Fibonacci Number
'''
Problem Description
Task. Given an integer 𝑛, find the last digit of the 𝑛th Fibonacci number 𝐹𝑛 (that is, 𝐹𝑛 mod 10).
Input Format. The input consists of a single integer 𝑛.
Constraints. 0 ≤ 𝑛 ≤ 107
.
Output Format. Output the last digit of 𝐹n
'''

def Fib_last_digit(n):
    if n<=1:
        return n
    elif (n==2):
        return 1
    else:
        num = 0
        a,b = 1,1
        for i in range(n-2):
            num = a + b
            num = num%10
            
            b = a
            a = num
            
        return num

n = int(input("n: "))

print('''{}th Fibonacci Number last digit is "{}"'''.format(n,Fib_last_digit(n)))
