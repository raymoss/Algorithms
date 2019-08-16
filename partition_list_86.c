struct ListNode {
      int val;
      struct ListNode *next;
};
 
typedef struct ListNode node;

node* partition_seq(node* head, int target){
    node* first_pointer = head;
    node* second_pointer = head;
    node* back_pointer = head;
    while(first_pointer){
        if(first_pointer->val >= target){
            break;
        }
        second_pointer = first_pointer;
        first_pointer = first_pointer->next;
    }
    if (second_pointer == head)
        back_pointer = NULL;
    else
    {
        back_pointer = second_pointer;
    }
    
    // find nodes greater than x
    while(first_pointer){
        if(first_pointer->val < target){
            if (back_pointer != NULL){
                node* temp = back_pointer->next;
                back_pointer->next = first_pointer;
                second_pointer->next = first_pointer->next;
                first_pointer->next = temp;
                first_pointer = second_pointer->next;
            }else{
                back_pointer = first_pointer;
                second_pointer->next = first_pointer->next;
                first_pointer->next = head;
                head = first_pointer;
                first_pointer = second_pointer->next;
            }
            
        }else{
            second_pointer = first_pointer;
            first_pointer = first_pointer->next;
        }
    }

    return head;
}