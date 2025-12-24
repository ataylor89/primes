# primes

## Introduction

The files in this repository use the Sieve of Eratosthenes algorithm to generate primes. The Sieve of Eratosthenes has been in use for a long time (allegedly, for over two thousand years).

The way it works is this. It creates an array of a specified size, with every slot set to 'P' except for the 0 and 1 slots, which are set to 'N'. Alternatively, we can use the values 0 and 1 or True and False, instead of 'P', 'C', and 'N'.

Then, we loop through the array. We start at index 2. If the current slot (element) is equal to 'P', then we create a nested loop that iterates over all multiples of the current index, which are greater than the current index and less than the size of the array, and sets these slots to 'C'.

In this way, we mark composite numbers composite, and leave prime numbers untouched.

In my program, I used the character values 'P', 'C', and 'N', to clearly distinguish which numbers are prime, composite, or neither.

It is also common to use the integer values 0 and 1, or the boolean values True and False.

The sieve (array) has to be large enough to accomodate the desired number of primes. If it's not large enough, we reconstruct a sieve that is ten times larger, until the sieve is large enough to accomodate the desired number of primes.

I hope this explains the algorithm. I had to play around with it for a while until I fully understood it. But after you understand it, you know a valuable algorithm that has been in use for over two thousand years.

## What is a sieve?

I want to quickly answer this vocabulary question. I had the same question myself in the past.

I think that "sieve" is a synonym for "filter". A filter is a device that separates an input stream into two categories: what gets filtered in and what gets filtered out.

The Sieve of Eratosthenes is a filter that separates primes from non-primes.

There are many other examples of sieves (filters). A kitchen colander is a type of sieve.

I hope this answers the vocabulary question.

## primes.c

The file primes.c can be compiled (and linked) with the command:

    gcc primes.c -o primes

Then, you can run the executable, with the command:

    ./primes <number_of_primes>

The string \<number_of_primes\> denotes the argument that you pass it. The argument has to be a positive integer.

For example,

    # This gets the first 5 primes
    ./primes 5

    # Now, let's get the first 10
    ./primes 10

    # Now, let's get the first 100
    ./primes 100

I actually created a symbolic link to the executable in my ~/bin folder.

    # First, I navigate to my ~/bin folder, which stores user programs (mostly by means of symbolic links)
    cd ~/bin

    # The code and executable are contained within my ~/Github/primes folder, so I use this directory to create the symbolic link
    ln -s ~/Github/primes/primes primes

    # Lastly, I have to make the primes file executable
    chmod +x ~/Github/primes/primes

    # Now, I can run the program from any directory, since ~/bin is included in my PATH variable
    primes 10
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29

## primetable.py

The file primetable.py uses the argparse library to parse command-line arguments and options.

Vocabulary happens to be one of my interests. What is the definition of "parser"?

A parser breaks a word, sentence, or file into its parts. It comes from the Latin word "pars, partis" which means "part" or "parts".

More specifically, a parser accepts an input, deciphers the input, and then produces a parse tree (or abstract syntax tree) that makes the input easier to work with and understand.

You can see how the argparse library makes it easier to work with, and understand, command-line arguments and options.

The file primetable.py can be used in many possible ways. Here are some examples:

    # Generate a list of primes, and save to file, without printing
    python primetable.py -n 10

    # Generate a list of primes, and save to file; print the last prime in the list
    python primetable.py -n 10 --show

    # Generate a list of primes, and save to file; print the full list of primes
    python primetable.py -n 10 --showlist

    # Generate a list of primes, save to file, and write a string representation to file
    python primetable.py -n 10 -o primes.txt

The files primetable.py and primes.c are very similar, because they both use the Sieve of Eratosthenes to generate a list of primes.

The two main differences between primetable.py and primes.c are the following:

1. The file primetable.py has a more advanced command-line interface
2. The file primetable.py saves the list of primes to a file, which effectively caches the result for future reference

It takes a long time to generate a hundred thousand primes (or a million... or ten million). For this reason, caching can be very useful. The file primetable.py caches each result in a local database, so that it only needs to use the SoE algorithm when the cache is insufficient.

I created a symbolic link to primetable.py in my bin folder, just like before.

    cd ~/bin
    ln -s ~/Github/primes/primetable.py primetable
    chmod +x ~/Github/primes/primetable.py

This way, I can run the program "primetable" from any directory.

    cd ~
    primetable -n 10 --showlist
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
