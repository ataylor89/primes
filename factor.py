#!/usr/bin/env python3

import argparse

def factor(n):
    arr = sieve(n + 1)
    primefac = {}
    for i in range(2, len(arr)):
        if arr[i] == 'P' and n % i == 0:
            primefac[i] = 0
            k = n
            while k % i == 0:
                k /= i
                primefac[i] += 1
    return primefac

def sieve(size):
    arr = ['P'] * size
    arr[0] = 'N'
    arr[1] = 'N'
    for i in range(2, size):
        if arr[i] == 'P':
            j = 2
            while i * j < size:
                arr[i * j] = 'C'
                j += 1
    return arr

def main():
    parser = argparse.ArgumentParser(prog='primecheck.py', description='Check if a number is prime')
    parser.add_argument('input', type=int)
    args = parser.parse_args()
    if args.input < 2:
        print('The input has to be a positive integer greater than 1')
        return
    primefac = factor(args.input)
    print(primefac)
    
if __name__ == '__main__':
    main()
