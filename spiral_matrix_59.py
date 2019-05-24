def adjust(i, j, input_value):
    if i < 0:
        i = 0
    if i >= input_value:
        i = input_value - 1
    if j < 0:
        j = 0
    if j >= input_value:
        j = input_value - 1
    return i, j

def generate_spiral_matrix(input_value):
    final_matrix = [[0]*input_value for i in range(input_value)]
    value = 0
    i = 0
    j = 0
    key = 0
    dic_direction = {0:[0, 1], 1:[1, 0], 2:[0, -1], 3:[-1, 0]}
    count = input_value*input_value
    deviation_flag = False
    while count != 0:
        while i >= 0 and i < input_value and j >= 0 and j < input_value :
            if final_matrix[i][j] != 0:
                deviation_flag = True
                break
            value += 1
            final_matrix[i][j] = value
            count -= 1
            # print(i, j, key)
            i += dic_direction[key][0]
            j += dic_direction[key][1]
        i, j = adjust(i, j, input_value)
        if deviation_flag:
            i -= dic_direction[key][0]
            j -= dic_direction[key][1]
            deviation_flag = False
        key += 1
        if key == 4:
            key = 0
        i += dic_direction[key][0]
        j += dic_direction[key][1]
    return final_matrix

for i in range(5):
    print(generate_spiral_matrix(i))