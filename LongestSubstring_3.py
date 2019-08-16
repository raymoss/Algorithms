def longest_substring(input_string):
    j = 0
    i = 0
    max_count = 0
    count = 0
    collected_items = set()
    while j < len(input_string):
        if input_string[j] in collected_items:
            j = i + 1
            if max_count < count:
                max_count = count
            collected_items.clear()
            count = 0
            i = i + 1
        else:
            collected_items.add(input_string[j])
            j = j+1
            count = count + 1
    if count > max_count:
        max_count = count
    return max_count

print(longest_substring(" "))
