def plus_one_actual(input_seq):
    carry = 1
    for i in range(len(input_seq) - 1, -1, -1):
        input_seq[i] += carry
        carry, input_seq[i] = divmod(input_seq[i], 10)
        if i == 0 and carry >= 1:
            input_seq.insert(0, carry) 
    return input_seq

input_seq = [9,9,9,9,9]
print(plus_one_actual(input_seq))