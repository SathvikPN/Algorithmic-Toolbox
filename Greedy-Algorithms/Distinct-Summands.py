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
    time.sleep(1.5)
    print(summands)
    for i in range(last_element+1,n+1):
        if i not in summands:
            
            print(f"{n} = {i} + {n-i}")
            if (n-i)==0:
                summands.append(i)
                time.sleep(1.5)
                print(f"All cutting of {i} excluding summands items done...")
                print(summands)
                time.sleep(1.5)
                return summands
            else:
                if (n-i) in summands:
                    time.sleep(1.5)
                    print(f"{i} NOT in summands \nBUT {n-i} in summands. \nSo,skipping this cutting")
                    time.sleep(1.5)
                    continue
                else:
                    time.sleep(1.5)
                    print(f"{i} NOT in summands. Appending {i}")
                    time.sleep(1.5)
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


