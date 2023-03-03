from tqdm import tqdm
from fichier import actions

capacity = 500*100
data = actions('data_Set')
list_stock = data[0]
val = data[1]
benefice = data[2]
n = len(val)


def algo_optimized(capacity, benefice, val, n, list_stock):
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    for i in tqdm(range(n + 1)):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif val[i-1] <= w:
                K[i][w] = max(benefice[i-1] + K[i-1][w-int(val[i-1])],
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    liste_action = []
    m = capacity
    y = n
    while m >= 0 and y >= 0:
        if K[y][m] == benefice[y-1] + K[y-1][m-int(val[i-1])]:
            liste_action.append(list_stock[y-1])
            m = m - int(val[i-1])
        y = y - 1
    return K[n][capacity], liste_action


print(algo_optimized(capacity, benefice, val, n, list_stock))
