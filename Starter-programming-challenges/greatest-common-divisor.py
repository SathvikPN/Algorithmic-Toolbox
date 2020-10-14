def gcd(numbers):
    a = numbers[0]
    b = numbers[1]
    smaller = a if a<b else b
    bigger = a+b-smaller
    if smaller==0:
        return bigger
    else:
        r= -1
        while (r!=0):
            q = bigger // smaller
            r = bigger % smaller
        
            bigger = (smaller*q)+r
        
            bigger = smaller
            smaller = r
        return bigger

def gcd_naive(numbers):
    a = numbers[0]
    b = numbers[1]
    smaller = a if a<b else b
    if ((a==0)and(b==0)):
        return ("NOT DEFINED")
    elif smaller==0:
        return a+b-smaller
    else:
        while (smaller>0):
            if((a%smaller==0) and (b%smaller==0)):
                return smaller
            smaller = smaller - 1
        return ("terminated")

    
print('''GCD Calculator
Enter two numbers (both not ZERO) separated by a space''')
n = input().split()
numbers = []
for i in range(2):
    numbers.append(int(n[i]))
print("Using Naive Method GCD is",gcd_naive(numbers))
print("Using Euclid Algorithm GCD is",gcd(numbers))

