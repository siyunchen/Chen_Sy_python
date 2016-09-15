# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:35:52 2016

@author: SiyunChen
"""

'''
# Q1 Define a function max()that takes two numbers as arguments 
     and returns the largest of them.
'''
def print_max(a, b): 
#  Define a function to find out the maximum of two numbers.    
    if a > b: 
        print(a, 'is the maximum') # If a > b, a is the maximum of two numbers.
    elif a == b:
        print(a,'is equal to', b) # If a quals to b, a = b.
    else:
        print(b, 'is the maximum') # If a < b, b is the maximum of two numbers.

print_max(4, 10) 
# call the function

print_max(5,5) 
# call the function again


''' 
# Q2 Define a function max_of_three()that takes three numbers as arguments 
     and returns the largest of them.  
'''
def max_of_three(a, b, c):
# Define a function to find out the maximum of three numbers.
 if a >= b:
   if a >= c:
      print(a, 'is the maximum of three')
      # If a > = b and a > c, a is the maximum of three numbers.
   else:
      print(c, 'is the maximum of three')
      # If a > = b and a < c, c is the maximum of three numbers.
 else:
  if b >= c:
      print(b, 'is the maximum of three')
      # If a < b and b > = c, b is the maximum of three numbers.
  else:
      print(c, 'is the maximum of three')
      # If a < b and b < c, c is the maximum of three numbers.

max_of_three(6, 1, 2) 
# call the function

max_of_three(9, 16 ,5) 
# call the function again


'''
# Q3 Define a function that computes the length of a given list or string.
'''
def length(inputString):
# Define a function to calculate the length of a string.
# inputString is a given list or string.
    count = 0 # Initializing the length to be equal to zero.
    for i in inputString: #for loop to repeat n number of times
        count = count + 1
    return count

print ('The length of the string is', length('Hello World')) 
# call the function

print ('The length of the string is', length('ThisisFun')) 
# call the function

print(length(""))
# call the function


'''
# Q4 Write a function that takes a character (i.e. a string of length 1) 
     and returns True if it is a vowel, False otherwise.  
'''
def is_a_vowel(inputString):
# Define a function to check if the character is a vowel or not.
# inputString is an alphabet character.
   vowels = ('a', 'e', 'i', 'o', 'u','A','E','I', 'O', 'U')
   # List all the vowels.
   if inputString in vowels:
     print ('True') # True if the character is in the vowels list.
   else:
     print('False') # False if the character is not in the vowels list.

is_a_vowel('a')
# call the function

is_a_vowel('b')
# call the function

is_a_vowel('A')
# call the function


'''
# Q5 Write a function translate()that will translate a text into 
     "rövarspråket" (Swedish for "robber's language").
'''
vowels = ('a', 'e', 'i', 'o', 'u','A','E','I', 'O', 'U', ' ')
# List all the vowels.
def translate(inputString):
# Define a function to translate the text.
  new = '' # Initializing the new text to null.
  for c in inputString: #for loop to repeat n number of times
   if c in vowels: 
    new = new + c # If the character in input strings is in vowels list, 
                  # adds character in inputString to the new text
                  # and assign the result to new text.
   else:
    new = new + c + 'o' + c 
  return new # If the character in input strings is not in vowels list, 
             # adds character in inputString to the new text, 
             # adds o between the character in inputString,
             # and adds character in inputString to the new text to new text
             # and assign the result to new text.

print('The translatd string is', translate('this is fun'))
# call the function 

print('The translatd string is', translate('This was good'))
# call the function


'''
# Q6 Define a function sum()and a function multiply()that sums 
     and multiplies (respectively) all the numbers in a list of numbers.
'''
def sum(inputNumbers):
# Define a function to find the sum of given list of numbers.
    total = 0 # Initializing the sum of numbers to be equal to zero.
    for number in inputNumbers: # for loop to repeat n number of times
        total = total + number # Add number in the inputString to the total 
                               # and assign the result to total. 
    return total
 
 
def multiply(inputNumbers):
# Define a function to find the muptiplication of given list of numbers.
     total = 1 # Initializing the multiplication of numbers to be equal to one.
     for number in inputNumbers: # for loop to repeat n number of times
         total = total * number # Multiply number in the inputString to the 
                                # totaland assign the result to total. 
     return total
 
print('The sum of the numbers is', sum([3, 4, 5, 6]))
print('The multiplication of the numbers is', multiply([3, 4, 5, 6]))
# call the function

print('The sum of the numbers is', sum([-13, 1, 2, 4]))
print('The multiplication of the numbers is', multiply([-13, 1, 2, 4]))
# call the function


'''
# Q7 Define a function reverse()that computes the reversal of a string.
'''
def reverse(inputString):
# Define a function to compute the the reversal of a string.
    result = [] # Initializing the result to null.
    for word in inputString.split()[::-1]: 
    # for loop to repeat n number of times.
    # Split each character in inputString from the last one to the first one.
        result.append(word[::-1])
    
    return " ".join(result) # Combine each character in the inputString from 
                            # the last character to the first one.

print(reverse('This was good ')) 
# call the function

print(reverse('This is fun'))
# call the function again


'''
# Q8 Define a function is_palindrome()that recognizes palindromes 
     (i.e. words that look the same written backwards).
'''
def is_it_palindrome(inputString):
# Define a function to recognizes the inputString is inputpalindromes or not.
    inputString = inputString.upper() # Take care of mixed case by uper casing
                                    # the word.
    inputString = inputString.replace(" ", "") # Take care of spaces.
    return inputString == inputString[::-1] 
    # True if the inputString that looks the same written backwards.
    # False if the inputString that looks different written backwards.
                                 
print(is_it_palindrome('Radar')) 
# call the function

print(is_it_palindrome('R adar2')) 
# call the function

print(is_it_palindrome('R adar')) 
# call the function again


'''
# Q9 Write a function is_member()that takes a value 
     (i.e. a number, string, etc) x and a list of values a, and returns True 
     if x is a member of a, False otherwise). 
'''
def is_member(x, a):
# Define a function to check if a value x  is member of a list a or not.
    if len(a) == 0:
        return False # False if there is no element in list a. 
    return x == a[0] or is_member(x, a[1:]) 
    # True if there is at least one the same element of x and a.

print(is_member(1,[1,2,3,4,5])) 
# call the function

print(is_member('b', [1, 2, 'a'])) 
# call the function

print(is_member('abcd', ['abcd', 'dfwe', 'rtw']))
# call the function


'''
# Q10 Define a function overlapping()that takes two lists and returns True 
      if they have at least one member in common, False otherwise.
'''
def overlapping(list1, list2):
# Defeine a function to check if two lists have at least one member in common.
    for element1 in list1: # for loop to repeat n number of times
        for element2 in list2: # for loop to repeat n number of times
            if element1 == element2:
                return True # True if two lists have at least one member 
                            # in common.
    return False # False if two lists have no member in common.

print(overlapping([1, 2, 3], [2, 3, 4])) 
# call the function

print(overlapping([1, 'apple', 3], ['apple', 'boy', 'cat'])) 
# call the function again



'''
# Q11 Define a function generate_n_chars()that takes an integer n and 
      a character c and returns a string, n characters long, 
      consisting only of c:s.
'''
def generate_n_chars(n, c):
# Define a function to takes an integer n and a character c 
# and returns a string, n characters long, consisting only of c:s.
    outputString = '' # # Initializing the outputString to null.
    for i in range(n): # for loop to repeat n number of times
        outputString = outputString + c
        # Add number character c to outputString 
        # and assign the result to outputString. 
    return outputString

print ('The generated string is', generate_n_chars(2, 'c'))
# call the function

print ('The generated string is', generate_n_chars(5, 's'))
# call the function

print ('The generated string is', generate_n_chars(8, '*'))
# call the function


'''
# Q12 Define a procedure histogram()that takes a list of integers 
      and prints a histogram to the screen. 
'''
def histogram(IntegerList):
# Define a function to  take a list of integers 
# and prints a histogram to the screen. 
    for n in IntegerList: # for loop to repeat n number of times
     print(generate_n_chars(n, '*')) # Using generate_n_chars from Q13.
   
histogram([1, 2, 3])
# call the function

histogram([6, 5, 4, 3, 7])
# call the function

histogram([6, 1, 8, 9, 10, 2])
# call the function


'''
# Q13 Write a function max_in_list()that takes a list of numbers 
      and returns the largest one.  
'''
def max_in_list(inputList):
# Define a function to take a list of numbers and returns the largest one.  
    max = inputList[0] # Initializing inputList
    for m in inputList: # for loop to repeat n number of times
        if m > max:
            max = m # If m in inputList > the max of the list, assign m to max.
    return max

print('The largest one is', max_in_list([1, 2, 3, 4])) 
# call the function
print('The largest one is', max_in_list([5, 1, 39, -1, 19])) 
# call the function again


'''
# Q14 Write a program that maps a list of words into a list of integers
      representing the lengths of the correponding words.
'''
def map_list_to_integers(inputWords):
# Define a function to map a list of words into a list of integers
# representing the lengths of the correponding words.
    lengths = [] # Initializing the lengths
    for word in inputWords: # for loop to repeat n number of times
     lengths.append(len(word)) # Add length of word in inputWords to length.
    return lengths

inputWords = ['Happy', 'Everyday', 'Friends']
print ('The list of integers is',map_list_to_integers(inputWords))
# call the function

inputWords = ['Good', 'Evening', 'Classmates']
print ('The list of integers is', map_list_to_integers(inputWords))
# call the function


'''
# Q15 Write a function find_longest_word()that takes a list of words 
      and returns the length of the longest one.  
'''
def map_list_to_integers(inputWords):
    lengths = []
    for word in inputWords: # for loop to repeat n number of times
     lengths.append(len(word))
    return lengths
# Using the function from Q14.
    
def find_longest_word(inputWords):
# Define a function to take a list of words 
# and return the length of the longest one.  
    return max(map_list_to_integers(inputWords))
    
print('The length of the longest word is', 
      find_longest_word(['Happy', 'Everyday', 'Friends'])) 
# call the function

print('The length of the longest word is', 
      find_longest_word(['Good', 'Evening', 'Classmates']))
# call the function
           

'''
# Q16 Write a function filter_long_words()that takes a list of words 
      and an integer n and returns the list of words that are longer than n.
'''
def filter_long_words(inputWordsList, n):
# Define a function to takes a list of words 
# and an integer n and returns the list of words that are longer than n.
   return [word for word in inputWordsList if len(word) > n]

print('The list of words is', 
      filter_long_words(['zoo', 'cats','zebra','ok'],3)) 
# call the function
      
print('The list of words is', 
      filter_long_words(['a', 'wonderful','place','to', 'visit'],4)) 
# call the function