from fichier1 import actions

data = actions('data_Set')
list_stock = data[0]
capacity = 500
val = data[1]
benefit = data[2]
n = len(val)
t = [[-1 for i in range(capacity + 1)] for j in range(n+1)]

def force_brute(val, benefit, capacity, n):
    """
    This function makes it possible to produce the result of the best 
    possible benefit with the maximum investment.
    """
    #base conditions
    if n == 0 or capacity == 0:
        return 0

    if t[n][capacity] != -1:
        return t[n][capacity]
    # choice diagram code
    if val[n-1] <= capacity:
        t[n][capacity] = max(benefit[n-1] + force_brute(val, benefit, 
        capacity - int(val[n-1]), n-1), force_brute(val, benefit, capacity, n-1))
        return t[n][capacity]  
    elif val[n-1] > capacity:
        t[n][capacity] = force_brute(val, benefit, capacity, n-1)
        return  t[n][capacity]

print(force_brute(val, benefit, capacity, n))

res = t[n][capacity]
w = capacity
"""
This loop allows you to list all the actions purchased, 
to obtain the best benefit.
"""
for i in range(n, 0, -1):
    if res <= 0:
        break
    if res == t[i - 1][w]:
        continue
    else:        
        res = res - benefit[i - 1]
        
        if res >= 0:
            w = w - int(val[i - 1])
            print(list_stock[i - 1], val[i - 1], benefit[i - 1], w)
print(capacity-w)
