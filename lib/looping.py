#!/usr/bin/env python3

def happy_new_year():
    i=10
    while i>0:
        print(i)
        i-=1
    print("Happy New Year!")

def square_integers(int_list):
    squared = [square_integers * square_integers for square_integers in int_list]
    return squared

def fizzbuzz():
    for i in range(100):
        if (not (i+1)%15):
            print("FizzBuzz")
        elif (not (i+1)%3):
            print("Fizz")
        elif (not (i+1)%5): 
            print("Buzz")
        else: 
            print(i+1)
        