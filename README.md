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

    # Generate a list of the first 10 primes, and store the result, without printing
    python primetable.py 10

    # Generate a list of the first 10 primes, and print the 10th prime
    python primetable.py 10 --shownth

    # Generate a list of the first 10 primes, and print the list
    python primetable.py 10 --showlist

    # Generate a list of the first 10 primes, and write the list to file
    python primetable.py 10 --showlist -o primes.txt

    # Generate a list of the first 100 primes, store the result, print the list, and clock the time it takes
    python primetable.py 100 --showlist --time

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

## primecheck.py

The file primecheck.py checks whether a number is prime.

It accepts an integer as a positional argument.

If the argument is less than 2, then the program indicates that it is neither prime nor composite.

If the argument is greater than or equal to 2, then the program indicates whether it is prime or composite.

Here is a fun fact. A prime number has exactly two factors. For example, 2 has the factors 2 and 1. 5 has the factors 5 and 1.

A composite number, on the other hand, has more than two factors. For example, 10 has the factors 1, 2, 5, and 10.

The file primecheck.py uses the Sieve of Eratosthenes algorithm to generate a prime sieve. It then uses the prime sieve to determine whether a positive integer is prime or composite. The prime sieve is an array of character values: 'P', 'C', and 'N'.

For example, let prime_sieve be the name of our prime sieve. Then prime_sieve[2] is set to 'P', and prime_sieve[10] is set to 'C'. Since 0 and 1 are neither prime nor composite, the values prime_sieve[0] and prime_sieve[1] are set to 'N'.

You can see that, after our prime sieve is generated, the program can look up a number's primality in constant time.

We see that... the Sieve of Eratosthenes algorithm has many uses. As shown thus far, it can be used to generate the first n primes, and it can also be used to check whether a number is prime. We will see, in a later section, that it can also be used to factor a number.

The file primecheck.py can be run with the following command:

    python primecheck.py <integer_argument>

For fun, let's test some of the odd numbers in the 190s interval.

    python primecheck.py 191
    191 is prime

    python primecheck.py 193
    193 is prime

    python primecheck.py 197
    197 is prime

    python primecheck.py 199
    199 is prime

    python primecheck.py 201
    201 is composite

You can see that the 190s interval is rich with primes. (So is the 10s interval.)

    python primecheck.py 11
    11 is prime

    python primecheck.py 13
    13 is prime

    python primecheck.py 17
    17 is prime

    python primecheck.py 19
    19 is prime

    python primecheck.py 21
    21 is composite

If we take any interval of ten consecutive positive integers, there will be five odd numbers and five even numbers. One of the odd numbers will be divisible by 5. Thus, an interval like this can have four primes at most.

I thought I would end this section with a cool theorem :)

Also, I would like to mention that I created a symbolic link for primecheck in my ~/bin folder.

    cd ~/bin
    ln -s ~/Github/primes/primecheck.py primecheck
    chmod +x ~/Github/primes/primecheck.py

Now, let's move onto the next section.

## Interlude

Number theory is a rich subject in mathematics. I thought I would ask some interesting number theory questions in an interlude.

1. Is the number of primes finite or infinite?
2. Is it possible to find a sequence of n consecutive positive integers that has zero primes, for any positive integer n? (For example, can you find a sequence of 100 consecutive positive integers that has zero primes, or must there be at least one prime in this sequence?)

I learned the answer to question #1 a long time ago (in high school, or before high school).

I actually looked up the answer to question #2 today.

These are some really interesting questions in number theory. I thought that I would write them down.

Both of these questions teach us about the importance of mathematical proof. Each question has an answer, a correct answer. Each question has an answer that can be verified by mathematical proof.
