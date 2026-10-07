class item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

arr = [item(100, 20), item(60, 10), item(100, 50), item(200, 50)]

arr.sort(key = lambda x : x.value / x.weight, reverse=True)
t_profit = current_weight = 0
w = 90

for i in range(0, len(arr)):
    if current_weight+arr[i].weight <= w:
        current_weight += arr[i].weight
        t_profit += arr[i].value

    else:
        remaining = w - current_weight
        cost = (arr[i].value / arr[i].weight) * remaining
        t_profit += cost

print(t_profit)