def get_integer_cube_root(input_value):
    if input_value == 0:
        return 0
    left, right = 1, input_value
    while(left <= right):
        mid = (left + right) // 2
        if ( mid*mid*mid > input_value ):
            right = mid - 1
            continue
        if (mid*mid*mid < input_value):
            if (pow(mid + 1,3) > input_value):
                return mid
            left = mid + 1
            continue
    return 0

print(get_integer_cube_root(7))