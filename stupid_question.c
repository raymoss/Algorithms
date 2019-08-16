#include <stdio.h>

unsigned char reverse_nos(unsigned char num){
    unsigned char mask = 0x1;
    unsigned char result = 0x0;
    for(int i = 0; i < 7; i++){
        result |= mask & num;
        num = num >> 1;
        result = result << 1; 
    }
    return result;
}

int main(){
    printf("Reversed nos of %x is %x\n",0x34, reverse_nos(0x34));
    return 0;
}