#funkcyjnie
#def plecakFunctional(capacity, items):
#    def plecakRecFunctional(remainingCapacity, index):
#        if index == len(items) or remainingCapacity == 0:
#            return 0, []
#
#        value, weight = items[index]
#        
#        withoutValue, withoutItems = plecakRecFunctional(remainingCapacity, index + 1)
#        
#        if weight <= remainingCapacity:
#            withValue, withItems = plecakRecFunctional(remainingCapacity - weight, index + 1)
#            withValue += value
#            withItems = [items[index]] + withItems
#
#            if withValue > withoutValue:
#                return withValue, withItems
#
#        return withoutValue, withoutItems
#
#    maxValue, selectedItems = plecakRecFunctional(capacity, 0)
#    return maxValue, selectedItems
#
#items = [(60, 10), (100, 20), (120, 30)]
#capacity = 50
#print(plecakFunctional(capacity, items))


def plecakProcedural(capacity, items):
    n = len(items)
    dp = [[0 for i in range(capacity + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        value, weight = items[i - 1]
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]

    selectedItems = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selectedItems.append(items[i - 1])
            w -= items[i - 1][1]

    maxValue = dp[n][capacity]
    return maxValue, selectedItems

items = [(60, 10), (100, 20), (120, 30)]
capacity = 50
print(plecakProcedural(capacity, items))