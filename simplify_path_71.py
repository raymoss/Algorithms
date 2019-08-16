def create_path(segment_array):
    final_path = "/"
    for i in segment_array[:-1]:
        final_path += i + "/"
    return final_path + segment_array[-1]

def simplify_path(input_string):
    final_path = []
    segments = input_string.split("/")
    for i in segments:
        if i == "..":
            if len(final_path) > 0:
                final_path.pop()
            continue
        if i == ".":
            continue
        if i == "":
            continue
        final_path.append(i)
    return create_path(final_path)

print(simplify_path("/a/../../b/../c//.//"))
    
