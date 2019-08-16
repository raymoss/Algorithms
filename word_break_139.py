def helper(input_seq, word_dict, dp, index):
    length_seq = len(input_seq)
    if index >= len(input_seq):
        return True
    if input_seq[index] in word_dict.keys():
        for i in word_dict[input_seq[index]]:
            fail = False
            for j in range(len(i)):
                if index + len(i) < length_seq:
                    if input_seq[index + j] != i[j]:
                        fail = True
                        break
                else:
                    fail = True
                    break
            if not fail:
                if helper(input_seq, word_dict, dp, index + j + 1):
                    return True
    return False

def word_break(input_seq, words):
    word_dict = {}
    dp = {}
    for i in range(len(words)):
        if words[i][0] in word_dict.keys():
            word_dict[words[i][0]].append(words[i])
        else:
            word_dict[words[i][0]] = [words[i]]
    return helper(input_seq, word_dict, dp, 0)
input_string ="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
word = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(word_break(input_string, word))
#print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat","og"]))