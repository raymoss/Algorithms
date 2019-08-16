def add_integer_to_linked_list(node):
    if node.next == None:
        node.val += 1
        if node.val >= 10:
            carry, node.val = divmod(node.val, 10)
            return carry
        else:
            return 0
    carry = add_integer_to_linked_list(node.next)
    node.val += carry
    if node.val >= 10:
        carry, node.val = divmod(node.val, 10)
        return carry
    return 0