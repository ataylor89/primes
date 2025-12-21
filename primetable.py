import pickle
import os
import time
import argparse

table = []

def generate(n):
    size = 10 * n
    s = sieve(size)
    while s.count('P') < n:
        size *= 10
        s = sieve(size)
    table.clear()
    table.extend([i for i, j in enumerate(s) if j == 'P'][0:n])

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

def load(path='primetable.pickle'):
    if os.path.exists(path):
        with open(path, 'rb') as file:
            table.clear()
            table.extend(pickle.load(file))

def save(path='primetable.pickle'):
    if len(table) > 0:
        with open(path, 'wb') as file:
            pickle.dump(table, file)

def main():
    parser = argparse.ArgumentParser(prog='primetable.py', description='Create a prime table')
    parser.add_argument('-n', '--numberofprimes', type=float, required=True)
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-s', '--show', action='store_true')
    group.add_argument('-sl', '--showlist', action='store_true')
    parser.add_argument('-o', '--outputfile', type=str)
    args = parser.parse_args()
    try:
        n = int(args.numberofprimes)
        assert n > 0
    except:
        print('Unable to parse the command-line argument as a positive integer')
        return
    load()
    if len(table) < n:
        st = time.time()
        generate(n)
        te = time.time() - st
        save()
        print('Created a prime table with %d primes in %s seconds' %(n, te))
    if args.show:
        nthprime = table[n-1]
        if args.outputfile:
            with open(args.outputfile, 'w') as file:
                file.write(str(nthprime))
        else:
            print(nthprime)
    elif args.showlist:
        primes = table[0:n]
        if args.outputfile:
            with open(args.outputfile, 'w') as file:
                file.write(str(primes))
        else:
            print(primes)

if __name__ == '__main__':
    main()
