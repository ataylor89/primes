#!/usr/bin/env python3

import argparse

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
    n = args.input
    if n < 2:
        print('%d is neither prime nor composite' %n)
        return
    arr = sieve(n + 1)
    if arr[n] == 'P':
        print('%d is prime' %n)
    else:
        print('%d is composite' %n)

if __name__ == '__main__':
    main()
