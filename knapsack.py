'''There are N items, numbered 1,2,…,N. For each i (1≤i≤N), Item i has a weight of wi​ and a value of

vi​.

Taro has decided to choose some of the
N items and carry them home in a knapsack. The capacity of the knapsack is W, which means that the sum of the weights of items taken must be at most

W.

Find the maximum possible sum of the values of items that Taro takes home.
Constraints

    All values in input are integers.

1≤N≤100
1≤W≤10**5
1≤wi​≤W
1≤vi​≤10'''
def fractional_knsapsack(items,capacity):
    items.sort(key= lambda x: x[1],reverse=True)
    total_value=0
    for weight,value in items:
        if capacity>=weight:
            total_value+=value
            capacity-=weight
        else:
            pass
    return total_value
N, W = map(lambda x: int(float(x)), input().strip().split())
items = []
for _ in range(N):
    weight, value = map(float, input().strip().split())
    items.append((weight, value))
print(fractional_knsapsack(items,W))