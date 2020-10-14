def lcm(numbers):
    a = numbers[0]
    b = numbers[1]
    smaller = a if a<b else b
    bigger = a+b-smaller
    if smaller==0:
        return 0
    else:
        i = 2
        b = bigger
        s = smaller
        while(bigger%smaller!=0):
            bigger = b*i
            i=i+1
        return bigger
             
print('''LCM Calculator
Enter two numbers (both not ZERO) separated by a space''')
n = input().split()
numbers = []
for i in range(2):
    numbers.append(int(n[i]))

print("LCM is",lcm(numbers))
