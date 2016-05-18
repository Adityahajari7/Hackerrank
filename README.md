# Hackerrank

Sherlock and The Beast

Sherlock Holmes suspects his archenemy, Professor Moriarty, is once again plotting something diabolical. Sherlock's companion, Dr. Watson, suggests Moriarty may be responsible for MI6's recent issues with their supercomputer, The Beast.

Shortly after resolving to investigate, Sherlock receives a note from Moriarty boasting about infecting The Beast with a virus; however, he also gives him a clue—a number, . Sherlock determines the key to removing the virus is to find the largest Decent Number having digits.

A Decent Number has the following properties:

    Its digits can only be 3's and/or 5's.
    The number of 3's it contains is divisible by 5.
    The number of 5's it contains is divisible by 3.
    If there are more than one such number, we pick the largest one.

Moriarty's virus shows a clock counting down to The Beast's destruction, and time is running out fast. Your task is to help Sherlock find the key before The Beast is destroyed!

Constraints



Input Format

The first line is an integer, , denoting the number of test cases.

The subsequent lines each contain an integer, , detailing the number of digits in the number.



Print the largest Decent Number having digits; if no such number exists, tell Sherlock by printing -1.

#Sherlock and Squares

Watson gives two integers (A and B) to Sherlock and asks if he can count the number of square integers between A and B (both inclusive).

#
Find Digits
Given an integer,N, traverse its digits (d1,d2,...,dn) and determine how many digits evenly divide N(i.e.: count the number of times N divided by each digit d1 has a remainder of 0). Print the number of evenly divisible digits.

Note: Each digit is considered to be unique, so each occurrence of the same evenly divisible digit should be counted (i.e.: for N = 111, the answer is 3 ).

#Arrays

An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, , of size , each memory location has some unique index, (where ), that can be referenced as (you may also see it written as ).

Given an array, , of integers, print each element in reverse order as a single line of space-separated integers.

