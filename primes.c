#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* sieve(int size) {
    char* numbers = malloc(sizeof(char)*size);
    memset(numbers, 'P', size);
    numbers[0] = '0';
    numbers[1] = '1';
    for (int i = 2; i < size; i++) {
        if (numbers[i] == 'P') {
            for (int j = 2; i*j < size; j++) {
                numbers[i*j] = 'C';       
            }
        } 
    }
    return numbers;
}

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Usage: %s <number_of_primes>\n", argv[0]);
        return 0;
    }
    int n = atoi(argv[1]);
    int count = 0;
    char* numbers = sieve(1000);
    for (int i = 2; i < 1000 && count < n; i++) {
        if (numbers[i] == 'P') {
            count++;
            if (count < n) {
                printf("%d, ", i);
            }
            else {
                printf("%d\n", i);
            }
        }
    }
    return 0;
}
