#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Sieve {
    char* table;
    int size;
    int num_primes;
};

struct Sieve sieve(int size) {
    struct Sieve s;
    s.table = malloc(sizeof(char)*size);
    memset(s.table, 'P', size);
    s.table[0] = '0';
    s.table[1] = '1';
    s.size = size;
    s.num_primes = size - 2;
    for (int i = 2; i < size; i++) {
        if (s.table[i] == 'P') {
            for (int j = 2; i*j < size; j++) {
                if (s.table[i*j] == 'P') {
                    s.table[i*j] = 'C';
                    s.num_primes--;
                }
            }
        } 
    }
    return s;
}

int* generate(int n) {
    struct Sieve s;
    int size = 10 * n;
    s = sieve(size);
    while (s.num_primes < n) {
        size *= 10;
        s = sieve(size);
    }
    int* primes = malloc(sizeof(int)*n);
    int counter = 0;
    for (int i = 0; i < size; i++) {
        if (s.table[i] == 'P') {
            primes[counter] = i;
            counter++;
        }
    }
    return primes;
}

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Usage: %s <number_of_primes>\n", argv[0]);
        return 0;
    }
    int n = atoi(argv[1]);
    if (n < 1) {
        printf("The input has to be a positive integer\n");
        return 0;
    }
    int* primes = generate(n);
    for (int i = 0; i < n; i++) {
        if (i < n - 1) {
            printf("%d, ", primes[i]);
        }
        else {
            printf("%d\n", primes[i]);
        }
    }
    return 0;
}
