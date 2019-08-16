def longest_pallindrome(input_seq1):
    if len(input_seq1) == 0:
        return 0
    grid = [[0]*len(input_seq1) for i in range(len(input_seq1))]
    max_count = 0
    count = 0
    start_ind = 0
    end_ind = 0
    for k in range(len(input_seq1)):
        for i, j in zip(range(len(input_seq1) - k), range(k , len(input_seq1) + k)):
            if i == j:
                max_count = 1
                grid[i][j] = True
                start_ind = i
                end_ind = j
            elif j == i + 1 and input_seq1[i] == input_seq1[j] :
                max_count = 2
                grid[i][j] = True
                start_ind = i
                end_ind = j
            elif input_seq1[i] == input_seq1[j] and grid[i+1][j-1]:
                grid[i][j] = True
                if j - i + 1 > max_count:
                    max_count = count
                    start_ind = i
                    end_ind = j
    return input_seq1[start_ind: end_ind + 1]

print(longest_pallindrome("cabba"))
            

