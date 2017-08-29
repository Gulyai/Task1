import time
import copy
import random

def hello(arg):
    """
    basic 1
    """
    print("Hello, %s!" % arg)
    
def sum(user_list):
    """
    basic 2
    """
    result = 0
    for num in user_list:
        result += num
    return result

def multiply(user_list):
    """
    basic 3
    """
    result = 1
    for num in user_list:
        result *= num
        
    return result

def reverse(user_string):
    """
    basic 3
    """
    result = ''
    
    for i in range(len(user_string) - 1, -1, -1):
        result += user_string[i]
    return result

def reverse2(user_string):
    """
    basic 3
    """
    return user_string[::-1]

def is_palindrome(word):
    """
    basic 4
    """
    end = -1
    for i in range(0, len(word)//2 + 1):
        if word[i] != word[end]:
            return False
        end -= 1
    return True

def histogram(list_of_integers):
    """
    basic 5
    """
    for integer in list_of_integers:
        print("*" * integer)
        
def caesar_cipher():
    """
    basic 6
    transforms only english letters
    """
    string = input("Type a string: ")
    key = int(input("Type a key: "))
    print("Transforming", end = '')
    result = ''
    for char in string:
        if ord(char) > 64 and ord(char) < 91:
            if (ord(char) + key) > 90:
                result += chr(ord(char) + key - 26)
            elif (ord(char) + key) < 65:
                result += chr(ord(char) + key + 26)
            else:
                result += chr(ord(char) + key) 
        elif ord(char) > 96 and ord(char) < 123:
            if (ord(char) + key) > 122:
                result += chr(ord(char) + key - 26)
            elif (ord(char) + key) < 97:
                result += chr(ord(char) + key + 26)
            else:
                result += chr(ord(char) + key)
        else:
            result += char
    print(".", end = '')
    time.sleep(0.5)
    print(".", end = '')
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    return result 


def diaginal_reverse(matrix):
    """
    basic 7
    """
    result = copy.deepcopy(matrix)
    for n in range(len(matrix)):
        for m in range(len(matrix[n])):
            if n == m:
                continue
            else:
                result[n][m] = matrix[m][n]
                
    return result

def game():
    """
    basic 8
    """
    while True:
        start = int(input("Starting point: "))
        end = int(input("Ending number: "))
        if start < end:
            break
        else:
            print("Wrong range! Try again!")
            
    secret_number = random.randint(start, end)
    while True:
        guess_number = int(input("Try to guess secret number: "))
        if guess_number == secret_number:
            print("You win!")
            break
        else:
            print("Try again!")
            
def brackets_checker(user_string):
    """
    basic 9
    """
    brackets_list = []
    for char in user_string:
        if char == "[":
            brackets_list.append(char)
        elif char == "]":
            if len(brackets_list) == 0:
                return False
            else:
                brackets_list.pop()
                
    return len(brackets_list) == 0
    
    
def char_freq(word):
    """
    basic 10
    """
    result = dict()
    for char in word:
        if char in result:
            result[char] += 1
        else:
            result[char] = 0
                  
    return result
        
def dec_to_bin(num):
    """
    basic 11
    """
    return bin(num)

def ship_battle():
    """
    basic 12
    """
    while True:
        matrix_order = int(input("Matrix Order: "))
        if matrix_order > 0:
            break
        else:
            print("Wrong matrix order! Try again!")
            
    print("Battle field looks like this:")
    for i in range(0, matrix_order + 1):
        if i == 0:
            print(" ", end = ' ')
            continue
        print(i, end = " ")
    print()
    for a in range(1, matrix_order + 1):
        print(a, end = " ")
        for x in range(matrix_order):
            print("X", end = " ")
        print()
    
    secret_ship = [random.randint(0, matrix_order - 1), random.randint(0, matrix_order - 1)]
    while True:
        a, b = input("Try to guess possision of the ship: ").split()
        
        if [int(a) - 1, int(b) - 1] == secret_ship:
            print("You win!")
            
            break
        else:
            print("Try again!")



    
    

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
