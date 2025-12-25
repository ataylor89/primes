#!/usr/bin/env python3

import argparse
import pickle
import time
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
default_cache_path = os.path.join(script_dir, 'primetable.pickle')

flags = {'used_cache': False}

def factor(n):
    assert isinstance(n, int) and n > 1, 'n must be a positive integer greater than 1'
    cache = load()
    if cache and len(cache) > 0 and n <= cache[-1]:
        primes = cache
        flags['used_cache'] = True
    else:
        primes = [i for i, j in enumerate(sieve(n+1)) if j == 'P']
        flags['used_cache'] = False
    primefac = {}
    for p in primes:
        if n == 1:
            break
        if n % p == 0:
            primefac[p] = 0
            while n % p == 0:
                n /= p
                primefac[p] += 1
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

def load(path = default_cache_path):
    if os.path.exists(path):
        with open(path, 'rb') as file:
            return pickle.load(file)

def main():
    parser = argparse.ArgumentParser(prog='factor.py', description='Factor a number')
    parser.add_argument('input', type=int)
    parser.add_argument('-t', '--time', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    n = args.input
    if n < 2:
        print('The input has to be a positive integer greater than 1')
        return
    st = time.time()
    primefac = factor(n)
    te = time.time() - st
    print(primefac)
    if args.time:
        print('Factored %d in %s seconds' %(n, te))
    if args.verbose:
        if flags['used_cache']:
            print('The prime numbers were loaded from file')
        else:
            print('The prime numbers were generated from a prime sieve')

if __name__ == '__main__':
    main()
