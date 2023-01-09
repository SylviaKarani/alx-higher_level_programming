#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        k = i % 5 == 0
        m = i % 3 == 0
        j = k and m
        mes = f"FizzBuzz" if j else f"Buzz" if k \
            else f"Fizz" if m else f"{i:d}"
        print(mes, end=" ")
