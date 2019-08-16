def binary_to_int(input):
    value = 0
    index = 0
    for i in range(len(input) - 1, -1,-1):
        if input[i] == '1':
            value += pow(2, index)
        index += 1
    print(value)
    return value

def int_to_binary(input):
    value = ""
    while input > 1:
        input, temp = divmod(input, 2)
        value = str(temp) + value
    if input == 0:
        return value
    return str(input) + value

def binary_add(input1, input2):
    return int_to_binary(binary_to_int(input1) + binary_to_int(input2))

print(binary_add("111","100"))