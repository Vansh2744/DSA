def fractional_knapsack(price_arr, weight_arr, capacity):
    values = [(price_arr[i], weight_arr[i], price_arr[i]/weight_arr[i]) for i in range(len(price_arr))]

    for i in range(len(values)):
        for j in range(i+1, len(values)-i-1):
            if values[i][2] < values[j][2]:
                values[i], values[j] = values[j], values[i]

    profit = 0.0

    for price, weight, per_kg in values:
        if capacity >= weight:
            capacity -= weight
            profit += price
        else:
            profit += capacity*per_kg

    print(profit)


prices = [20, 30, 40, 50, 60]
weights = [3, 4, 5, 6, 7, 8]

fractional_knapsack(prices, weights, 10)