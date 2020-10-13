#Naive approach - Iterating every possible combination
def max_pairwise_product1(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
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
        if ((j!=index)and(numbers[j]>biggest2)):
            biggest2 = numbers[j]

    max_product = (biggest1*biggest2)
    return max_product

if __name__ == '__main__':
    #input_n = int(input())
    print("max_pairwise_product")
    input_numbers = [int(x) for x in input("sequence: ").split()]
    print(max_pairwise_product2(input_numbers))
