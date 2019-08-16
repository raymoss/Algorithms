def helper(input_seq1, input_seq2, final_seq, ind1, ind2, ind3, dp):
    if ind1 >= len(input_seq1) and ind2 >= len(input_seq2) and ind3 >= len(final_seq):
        return True
    if (ind1, ind2, ind3) in dp.keys():
        return dp[ind1, ind2, ind3]
    if ind1 < len(input_seq1) and ind3 < len(final_seq):
        if input_seq1[ind1] == final_seq[ind3]:
            if helper(input_seq1, input_seq2, final_seq, ind1 + 1, ind2, ind3 + 1, dp):
                return True
    if ind2 < len(input_seq2) and ind3 < len(final_seq):
        if input_seq2[ind2] == final_seq[ind3]:
            if helper(input_seq1, input_seq2, final_seq, ind1, ind2 + 1, ind3 + 1, dp):
                return True
    dp[ind1, ind2, ind3] = False
    return False
def interleaving_string(input_seq1, input_seq2, final_seq):
    dp = {}
    return helper(input_seq1, input_seq2, final_seq, 0, 0, 0, dp)

print(interleaving_string("aabcc","dbbca","aadbbcbcac"))