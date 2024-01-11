#!/usr/bin/env python3

def greet_programmer():
    print (f"Hello, programmer!")
    
def greet(name="Naureen"):
    print(f"Hello, {name}!")
    
greet()
   

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
   
greet_with_default()

greet_with_default("Sunny")

def add(num1, num2):
    return num1 + num2

num1 = 45
num2 = 55

result = add(num1, num2)
print(result)


def halve(number):
    return number // 2

number = 100
result = halve(number)
print(result)


def halve(number):
    return number / 2

number = 100
result = halve (number)
print(result)



