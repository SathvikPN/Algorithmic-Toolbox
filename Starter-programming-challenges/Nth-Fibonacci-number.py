#nth Fibonacci number 1 1 2 3 5... n

def Fib(n):
    if n<=1:
        return n
    elif (n==2):
        return 1
    else:
        num = 0
        a,b = 1,1
        for i in range(n-2):
            num = a + b
            print("{} = {} + {}".format(num,a,b))
            b = a
            a = num
            
        return num

n = int(input("n: "))

print('''\n{}th Fibonacci Number is "{}"'''.format(n,Fib(n)))
        
    
