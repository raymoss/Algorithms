global req_seq_no
from math import factorial

def helper(input_seq, remaining_seq):
    global req_seq_no
    if len(remaining_seq) == 0:
        if req_seq_no == 1:
            return input_seq
        req_seq_no -= 1
        return []
    for i in range(len(remaining_seq)):
        input_seq.append(remaining_seq[i])
        temp = remaining_seq.pop(i)
        result_seq = helper(input_seq, remaining_seq)
        if len(result_seq) != 0:
            return result_seq
        input_seq.pop()
        remaining_seq.insert(i, temp)
    return []
    
def generate_permutation_seq(input_len, req_seq):
    global req_seq_no
    req_seq_no = req_seq
    if input_len == 0:
        return []
    input_seq = [0]*input_len
    for i in range(1, input_len + 1):
        input_seq[i - 1] = i
    return "".join(str(i) for i in helper([],input_seq))

def get_required_seq(input_value, req_seq):
    final_seq = ""
    input_list = [0]*input_value
    for i in range(len(input_list)):
        input_list[i] = i + 1

    while req_seq >= 2:
        fact_value = factorial(input_value - 1)
        temp = req_seq//fact_value
        if req_seq%fact_value == 0:
            temp = temp - 1
            final_seq += str(input_list.pop(temp))
            input_list.reverse()
            temp = "".join(str(i) for i in input_list)
            final_seq += temp
            return final_seq
        # print(temp)
        # print("input_list: ",input_list)
        final_seq += str(input_list.pop(temp))
        req_seq = req_seq%fact_value
        input_value -= 1
    temp = "".join(str(i) for i in input_list)
    final_seq += temp
    return final_seq


print(get_required_seq(4,9))