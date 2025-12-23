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

## primes.c

The file primes.c can be compiled (and linked) with the command:

    gcc primes.c -o primes

Then, you can run the executable, with the command:

    ./primes <number_of_primes>

The string \<number_of_primes\> denotes the argument that you pass it. The argument has to be a positive integer. For example,

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
