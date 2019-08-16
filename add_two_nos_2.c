/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode node;

node* add_two_linked_list(node* l1, node* l2){
    node* new_list = NULL;
    node* prev = NULL;
    int carry = 0;
    while(l1 || l2){
        node* temp = (node *)malloc(sizeof(node));
        temp->val = 0
        if (l1)
            temp->val = l1->val;
        if (l2)
            temp->val += l2->val;
        temp->val += carry;
        carry = (temp->val)/10;
        temp->val = temp->val % 10;
        if (prev != NULL)
            prev->next = temp;
        prev = temp;
        if (new_list == NULL)
            new_list = temp;
        if (l1)
            l1 = l1->next;
        if (l2)
            l2 = l2->next;
    }
    prev->next = NULL;
    if (carry != 0){
        node* temp = (node*)malloc(sizeof(node));
        temp->val = carry;
        temp->next = NULL;
        prev->next = temp;
    }
    return new_list;
}