def rotate_right(head, rotation_index):
    first_pointer = head
    second_pointer = head
    count = 1
    if head == None:
        return head
    while rotation_index != 0 and first_pointer.next != None:
        first_pointer = first_pointer.next
        rotation_index -= 1
        count += 1
    if rotation_index != 0:
        rotation_index = rotation_index%count
        rotation_index -= 1
        while rotation_index != 0 and first_pointer.next != None:
            first_pointer = first_pointer.next
            rotation_index -= 1
    while first_pointer.next != None:
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next
    first_pointer.next = head
    head = second_pointer.next
    second_pointer.next = None
    return head
    
    