# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 19:02:13 2016

@author: SiyunChen
"""

'''
HW 2 Groups E
'''
#Overall Comment: Very good exercise, the format and comments showed your deep understanding of the code and the problems you
#                 are trying to solve.
# Q1 
def lexicon_dic(inputWord):
    '''
    Define a funtion to work as dictionary.
    Parameters: 
    inputWord： a list of English words in the Python dictionary we input
    Return:
    translation of the list of  English words we input 
    '''
    lexicon_dic={"merry":"god", "christmas":"jul", "and":"och", 
                 "happy":"gott", "new":"nytt", "year":"år"}
    #list all the related English and Swedish words as a Python dictionary
    if inputWord in lexicon_dic: #if the input word is in lexicon dictionary
             return lexicon_dic.get(inputWord) #if the input word is in the lexicon dictionary, return to the given key in the lexicon dictionary
    else: #if the input word is not in lexicon dictionary
             return inputWord #if the input word is not in the lexicon dictionary, return to the original input word

def translate(inputText):
    '''
    Write a function translate()that takes a list of English words and returns a list of Swedish words.
    Parameters:
    inputText: 
    Returns:
    a list of Swedish words of the list of words we input
    '''
    words = inputText.split( ); #split the input text into words and take each word individually
    new = " " #the new text will be based on the input text
    for i in words:
        new = new + lexicon_dic(i) + " "
    return new #For any word in inputText, return the new + lexicon_dic(i) + " "

print("The translated words are", 
      translate("merry christmas and happy new year")) #call the function translate()
print("The translated words are", 
      translate("merry christmas but happy new year")) #call the function translate() again

# Q2
def char_freq(inputText):
    '''
     Write a function char_freq()that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency 
     listing as a Python dictionary.
     Parameters:
     inputText: a string we input
     Returns:
     a frequency listing of the characters contained in the string we input
    '''
    #Spaces, numbers and characters are all will be counted for frequency 
    dictionary = {} #Begin with an empty dictionary
    for i in inputText: #for in loop : the item i in input text is in this loop 
        dictionary[i] = dictionary.get(i,0)+1 #use dictionary.get(i,0) to get [i], if it is not found, returns 0.
        #When the character is found, add number 1. For the first time, fequency is 1; for the second time, frequency is 2, etc.
    return dictionary #Make the function return to each frequency.
    
char_freq("abbabbcdbdbcbdbabdbcbbabdb") #call the function char_freq()
char_freq("b bdb bdb bcb bcb bb bcb ") #call the function char_freq()
char_freq("bcbdbcbbdbcbddbcbdbcbd") #call the function char_freq()
   
# Q3 
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 
       'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 
       'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 
       'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 
       'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 
       'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 
       'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
#List all the keys will be used to translate input text.
def ROT_13(inputWords):
    '''In Python, the key for ROT-13 may be represented by means of the 
     following dictionary:  
     key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 
            'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 
            'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 
            'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 
            'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 
            'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 
            'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 
            'X':'K', 'Y':'L', 'Z':'M'}  
     Your task in this exercise is to implement an encoder/decoder of ROT-13.
     Parameters:
     inputWords: a string we input
     Returns:
     the encode/decode of the string we input
     '''
    newtext='' #the newtext is an empty string at the beginning
    for char in inputWords: #for each character in input word
        if char in key: #if the character of input word is in the key list
            newtext = newtext + key[char] #newtext + key[char] will be assigned to newtext
        else: #if the character of input word is not in the key list
            newtext = newtext + char #newtext + char will be assigned to newtext
    return newtext

print(ROT_13('Lbh ner zl Fhafuvar!')) #call the function ROT_13()
print(ROT_13('Clguba vf uneq.')) #call the function ROT_13()  
print(ROT_13('Python is hard.')) #call the function ROT_13()  
print(ROT_13('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!')) #call the function ROT_13()  
                
# Q4 
def correct(inputString): 
    '''
    Define a simple "spelling correction" function correct()that takes a string and sees to it that 1) two or more occurrences of the space
    character is compressed into one, and 2) inserts an extra space after a period if the period is directly followed by a letter.
    Parameters:
    inputString: a string we input
    Returns:
    the correction follwing the given principles of the string we input
    '''
    import re #import Regular expression operations to correct the input string
    correction = re.sub(' +',' ',inputString) #remove the extra spaces in the input strings by using substitution
    finalcorrection = re.sub('\.','. ',correction) #add a space after a period without space by using substitution
    print(finalcorrection) #print the final corrected strings which is a correct sentence by combining both of our corrections

correct("This  is    very funny and cool.Indeed!") #call the function correct()
correct("This is         very good!") #call the function correct()
 
# Q5 
def make_3sg_form(inputVerb):
    '''
    The third person singular verb form in English is distinguished by the suffix -s, which is added to the stem of the infinitive form: 
    run -> runs. A simple set of rules can be given as follows:  a. If the verb ends in y, remove it and add ies b. If the verb ends in o, 
    ch, s, sh, x or z, add es c. By default just add s  Your task in this exercise is to define a function make_3sg_form() which given a verb in 
    infinitive form returns its third person singular form.
    Parameters:
    inputVerb: a word (verb) we input 
    Returns:
    third person singular form of the word (verb) we input
    '''
    if inputVerb.endswith('y'): #if the input verb end with y
        newverb = inputVerb[:-1] + 'ies' #the newverb deletes the character y and replaces y with 'ies'
    elif inputVerb.endswith(('o','ch','s','sh','x','z')): #if the verb ends with o, ch, s, sh, x, or z
        newverb = inputVerb + 'es' #the newverb adds 'es' to the end of the word
    else: #for other input verbs
        newverb = inputVerb + 's' #directly add 's' to the end of the word
    print(newverb) #print the new verb created by the ways above

make_3sg_form("like") #call the function make_3sg_form()
make_3sg_form("fly") #call the function make_3sg_form()
make_3sg_form("brush") #call the function make_3sg_form()
make_3sg_form("fix") #call the function make_3sg_form()

# Q6 
def make_ing_form(verb):
    '''
    Define a function make_ing_form()which given a verb in infinitive form returns its present participle form. Test your function with words such 
    as lie, see, move and hug.
    Parameters:
    verb: a word (verb) we input 
    Returns:
    present participle form of the verb we input
    '''
    if verb.endswith('e'): #if the verb end with 'e'
       newverb = verb[:-1]+'ing' #return all characters in the input word except the last 'e', add 'ing' to the word
    elif verb.endswith('ie'): #if the verb end with 'ie'
       newverb = verb[:-2]+'ying' #return all characters in the input word except the last two 'ie', add 'ying' to the word
    elif (verb[-2] in 'aeiou') and (verb[-3] not in 'aeiou') and (verb[-1] 
         not in 'aeiou'): #if the word consist of consonant-vowel-consonant character form
       newverb = verb + verb[-1] + 'ing' #add the last character of the word to the word, add 'ing' to the word
    else: #for all other verbs
       newverb = verb +'ing' #add 'ing' to the input word
    return newverb

print(make_ing_form('do')) #call the function make_ing_form()
print(make_ing_form('hug')) #call the function make_ing_form()
print(make_ing_form('move')) #call the function make_ing_form()

# Q7 
def max_in_list(inputList):
    '''
    Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns the largest one. 
    Parameters:
    inputList: a list of numbers we input
    Returns:
    the largest number of the list we input
    '''
    largest=0 #initialize the largest   
    for i in inputList: 
        if i>= largest: #if i is larger than or equal to the largest number
            largest=i #i is the new largest number
    return largest #if i is less than the larges number, return this number the new largest number

max_in_list([1, 2, 3, 4, 5, 8]) #call the function max_in_list()
max_in_list([-1, 2, 3, 5, 5, 10]) #call the function max_in_list

# Q8
# First, using a for-loop
def map_list(inputWords):
    '''
    Write a program that maps a list of words into a list of integers representing the lengths of the correponding words. 
    Parameters: 
    inputWords: a list of words we input
    Returns:
    a list of integers representing the lengths of the correponding words in the list we input
    '''
    lengths = [] #start with an ampty list of lengths
    for word in inputWords: #for each word in the input words
        lengths.append(len(word)) #map the list of input words into a list of length (integers)
    return lengths #return to a new length

map_list(['statistics','math','world']) #call the function map_list()

# Second, using the higher order function map()
def map_list(inputWords):
    '''
    Write a program that maps a list of words into a list of integers representing the lengths of the correponding words. 
    Parameters: 
    inputWords: a list of words we input
    Returns:
    a list of integers representing the lengths of the correponding words in the list we input
    '''    
    return list(map(len,inputWords)) #return a list of length (integers) of the input list of words
    
map_list(['make','mathematics','fun']) #call the function map_list()

# Third, using list comprehensions
def map_list(inputWords):
    '''
    Write a program that maps a list of words into a list of integers representing the lengths of the correponding words. 
    Parameters: 
    inputWords: a list of words we input
    Returns:
    a list of integers representing the lengths of the correponding words in the list we input
    '''
    l = len(inputWords) #initialize the l (length of the word)
    list  =[len(inputWords[i]) for i in range(l)] #use len() to find the length of the input list of word
    return list
    
map_list(['you','are','doing','well']) #call the function map_list()

# Q9 
def find_longest_word(inputString):
    '''
    Write a function find_longest_word()that takes a list of words and returns the length of the longest one. 
    Use only higher order functions.
    Parameters:
    inputString: a list of words we input
    Returns:
    the length of the longest word of the list we input
    '''
    return max(list(map(len,inputString))) #len() is used to map the input string of words into a list of length (integers)
    # max() is used to  find the maximum number of that list of integers

find_longest_word(['math', 'statistics', 'world']) #call the function find_longest_word()
find_longest_word(['hello', 'world', 'wonderful']) #call the function find_longest_word()

# Q10 
def filter_long_words(inputString, n):
    '''
    Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an integer n and 
    returns the list of words that are longer than n. 
    Parameters:
    inputString: a list of words we input
    n: an integer we input
    Returns:
    the list of words of the list of words we input that are longer than n (the integer we input)
    '''
    return list(filter(lambda i: len(i) > n, inputString)) #use the given length n to find the words that longer than n in input string
    #return the list of words that the length is larger than n

print('The list of words is', 
      filter_long_words(['zoo', 'cats','zebra','ok'],3)) #call the function filter_long_words()
print('The list of words is', 
      filter_long_words(['a', 'wonderful','place','to', 'visit'],4)) #call the function filter_long_words()
      
# Q11 
lex_dic = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott",
           "new":"nytt", "year":"år"}
# list all the related English and Swedish words as a Python dictionary
def translate(inputWords):
    '''
    Use the higher order function map()to write a function translate() that takes a list of English words and returns a list of Swedish words.
    Parameters:
    inputWords: a list of English words we input
    Returns:
    a list of Swedish words
    '''
    return list(map(lambda x: lex_dic[x.lower()], inputWords)) #map the English words to a list of Swedish words by the rules in the lex dictionary

print(translate(["merry"])) #call the function translate()
print(translate(["merry", "christmas", "and", "happy", "new","year"])) #call the function translate()

# Q12 Implement the higher order functions map(), filter()and reduce(). 
# First, map()
def newmap(function,inputList):
    '''
    Define a function to work as map() function
    Parameters:
    function: a function we defined
    inputList: a list of numbers we input
    Returns:
    apply the function we dinfed to the list of numbers we input
    '''
    newlist=[] #start with an empty new list
    for i in inputList: #use for-loop
        newlist.append(function(i)) #apply function (i) to the input list
    return newlist #return a new list of input string under the function

newmap(lambda x: 1 + x,[1,2,3,4,5]) #call the function newmap()
newmap(lambda y: 3 - y,[1,2,3,4,5]) #call the function newmap()

# Second, filter()
def newfilter(function,inputList):
    '''
    Define a function to work as filter() function
    Parameters:
    function: a function we defined
    inputList: a list of numbers we input
    Returns:
    filter the numbers in the list of numbers we input that satisfy the function we defined
    '''
    newlist = [] #start with an empty new list
    for i in inputList: #use for loop
        if function(i) == True: #check if the item i is true
            newlist.append(i) #if it is true, then make it to the new list
    return newlist
    
newfilter(lambda x: x > 3, [1, 2, 3, 4, 5, 6]) #call the function newfilter()
newfilter(lambda y: y < 5, [0, 1 ,2, 3, 4, 7]) #call the function newfilter()

# Third, reduce()
def newreduce(function,inputList):
    '''
    Define a function to work as reduce() function
    Parameters:
    function: a function we defined
    inputList: a list of numbers we input
    Returns:
    reduce the number in the list of numbers we input that satisfies the function we defined
    '''
    accum = inputList[0]
    # initialize the accum 
    for i in inputList[1:]: #use for loop, each i in the input list starts from the second place in the input list
        accum = function(accum,i) #use the function with accume and i
    return accum

newreduce(max,[1,2,3,4,5,6]) #call the function newreduce()
newreduce(min,[1,2,3,4,5,6]) #call the function newreduce()

