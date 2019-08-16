def max_profit(input_seq):
    if len(input_seq) == 0:
        return 0
    profit = 0
    min_value = input_seq[0]
    i = 0
    for i in range(len(input_seq)):
        if input_seq[i] - min_value > profit:
            profit = input_seq[i] - min_value
        else:
            if input_seq[i] < min_value:
                min_value = input_seq[i]
    return profit

input_seq = [7,1,5,3,6,4]
print(max_profit(input_seq))
        