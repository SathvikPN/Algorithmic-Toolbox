'''
Maximum value of Loot Problem

Problem Introduction
A thief finds much more loot than his bag can fit. Help him to find the most valuable combination
of items assuming that any fraction of a loot item can be put into his bag.

Problem Description
Task. The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
Input Format. The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack.
The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the
value and the weight of 𝑖-th item, respectively.
Constraints. 1 ≤ 𝑛 ≤ 103
, 0 ≤ 𝑊 ≤ 2 · 106
; 0 ≤ 𝑣𝑖 ≤ 2 · 106
, 0 < 𝑤𝑖 ≤ 2 · 106
for all 1 ≤ 𝑖 ≤ 𝑛. All the
numbers are integers.
Output Format. Output the maximal value of fractions of items that fit into the knapsack. The absolute
value of the difference between the answer of your program and the optimal value should be at most
10−3
. To ensure this, output your answer with at least four digits after the decimal point (otherwise
your answer, while being computed correctly, can turn out to be wrong because of rounding issues).
Sample 1.
Input:
3 50
60 20
100 50
120 30
Output:
180.0000
To achieve the value 180, we take the first item and the third item into the bag.

'''


def get_opt_value(capacity,values,weights):
    value = 0
    value_per_weight = []

    for i in range(len(weights)):
        value_per_weight.append(values[i]/weights[i])

    print('Value-per-kg of item',value_per_weight)
        
    while((capacity!=0)and(len(value_per_weight)!=0)):        
        chooseIndex = value_per_weight.index(max(value_per_weight))
        
        putWeight = weights[chooseIndex]
        if(putWeight>capacity):
            excess = putWeight - capacity
            putWeight = putWeight - excess
            print(f"From {weights[chooseIndex]}kgs' pack --> took {putWeight} kgs")
            
            value = putWeight*value_per_weight[chooseIndex]
            return value
        else:
            capacity = capacity - putWeight

            print(f"From {weights[chooseIndex]}kgs' pack --> took {putWeight} kgs")
            
            value = value + (putWeight*value_per_weight[chooseIndex])
            del value_per_weight[chooseIndex]
            del weights[chooseIndex]
            del values[chooseIndex]
    return value
        
if __name__ == "__main__":
    
    data = list(map(int,input().split()))
    
    for line in range(data[0]):
        userData = list(map(int,input().split()))
        data = data + userData
    print("data",data)
    n,capacity = data[0:2]
    print("Knapsack capacity =",capacity)
    values = data[2:(2*n)+2:2] #last element in range not considered
    weights = data[3:(2*n)+3:2]
    print("Values",values)
    print("Weights",weights)
    opt_value = get_opt_value(capacity,values,weights)
    print(f"Optimum Value {opt_value:.4f}")
