#include<stdio.h>

bool helper(int* input_seq, int start_index, int end_index, int target){
    if (end_index < start_index) 
        return false;
    int middle = (end_index + start_index)/2 ;
    if (input_seq[middle] == target)
        return true;
    int backup_middle = middle;
    if (start_index == middle)
        return helper(input_seq, middle + 1, end_index, target);
    if(input_seq[start_index] == input_seq[middle]){
        start_index++;
        middle--;
    }    
    if(input_seq[start_index] < input_seq[middle] && start_index < middle){
        if(target >= input_seq[start_index] && target < input_seq[middle]){
            return helper(input_seq, start_index, middle - 1, target);
        }
        return helper(input_seq, backup_middle + 1, end_index, target);
    }
    if(input_seq[end_index] == input_seq[middle]){
        end_index--;
        middle++;
    }
    if(middle < end_index){
        if(target > input_seq[middle] && target < input_seq[end_index]){
            return helper(input_seq, middle + 1, end_index, target);
        }
    }    
    return false;
}

bool rotated_search(int* input_seq, int seq_size, int target){
    return helper(input_seq, 0, seq_size - 1, target);
}