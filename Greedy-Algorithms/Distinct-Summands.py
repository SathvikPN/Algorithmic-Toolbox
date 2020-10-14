# Uses python3
import sys
import time
import math
    
#This function has some error
def optimal_summands_recursive(n,summands):
    if n==0:
        summands.append(0)
        return summands
    
    #write your code here
    if len(summands)==0:
        last_element = 0
    else:
        last_element = summands[len(summands)-1]

    for i in range(last_element+1,n+1):
        if i not in summands:
            
           # print(f"{n} = {i} + {n-i}")
            if ((n-i)==0):
                summands.append(i)
                return summands
            elif (i==(n-i)):
                summands.append(n)
                return summands
            else:
                if (n-i) in summands:
                    
                    continue
                else:
    
                    summands.append(i)
                    break
    summands=optimal_summands_recursive(n-i,summands)
    return summands

'''
Not a greedy approach
Based on pattern
final list of k elements
1,2,3...(k-1) sequential (arithmetic progression)
last element donot belong to the progression.
Took our AP: 0,1,2.... s
used sum=(n/2) * [2a+(n-1)d]
n = no. elements in list
here a=0, d=1
so n^2-n-(2s)=0
solving for n (+ve value)
n = decimal
Take n --> integer part
Now we remove 0. Not needed for output
so no. elements in list k=n-1
From pattern, append 1,2,3...(k-1)  to list
for last element: s - sum(list)
append last element to list
Final list is ready!
'''

def optimal_summands(s):
    index = (1 + math.sqrt(1+(4*2*s)))/2
    index = int(index)
    k = index - 1
    summands=[]
    for i in range(1,(k-1)+1):
        summands.append(i)
    sumList = ((k-1)*(k-1+1))/2
    last_element = int(s - sumList)
    summands.append(last_element)
    return summands
   

if __name__ == '__main__':
    n = int(input())
    summands1=[]
    summands2=optimal_summands_recursive(n,summands1)

    '''
    summands = optimal_summands(n)
   
    if summands==summands2:
        print("Both Approaches same result")
    else:
        print(f"Algebraic approach --> {summands}")
        print("Recursive approach --> {summands2}")
    '''
    print(len(summands2))
    for x in summands2:
       print(x, end=' ')


