# Uses python3
import sys
import time
    

def optimal_summands(n,summands):
    if n==0:
        return summands
    
    #write your code here
    if len(summands)==0:
        last_element = 0
    else:
        last_element = summands[len(summands)-1]

    for i in range(last_element+1,n+1):
        if i not in summands:
            
            print(f"{n} = {i} + {n-i}")
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
    summands=optimal_summands(n-i,summands)

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = []
    summands = optimal_summands(n,summands)

    print(len(summands))
    for x in summands:
        print(x, end=' ')
