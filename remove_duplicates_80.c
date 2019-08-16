#include<stdio.h>

int remove_duplicate(int *input_seq, int input_size){
    int previous_num = -1;
    int current_count = 0;
    int total_count = 0;
    int current_pointer = 0;
    for (int i = 0; i < input_size; i++){
        if(previous_num == input_seq[i]){
            if(current_count < 2){
                total_count++;
                current_count++;
                input_seq[current_pointer] = input_seq[i];
                current_pointer++;
            }
        }else{
            previous_num = input_seq[i];
            input_seq[current_pointer] = input_seq[i];
            current_pointer++;
            current_count = 1;
            total_count++;
        }
    }
    return total_count;
}

int main(){
    int input_seq[] = [1,1,1,2,2,3,4,5,6,7,7,7];
    printf("%d\n",remove_duplicate(input_seq, 12));
    return 0;
}

