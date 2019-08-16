def distance(word1, word2):
    if len(word1) == 0 or len(word2) == 0:
        return len(word1) + len(word2)
    sol = [[0]*(len(word2) + 1) for i in range(len(word1) + 1)]
    for i in range(len(word1) + 1):
        for j in range(len(word2) + 1):
            if i == 0 or j == 0:
                sol[i][j] = i + j
                continue
            if word1[i - 1] == word2[j - 1]:
                sol[i][j] = sol[i-1][j-1]
            else:
                sol[i][j] = 1 + min(sol[i][j-1], sol[i - 1][j], sol[i-1][j-1])
    return sol[len(word1)][len(word2)]

print(distance("horse","ros"))