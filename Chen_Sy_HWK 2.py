# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 19:02:13 2016

@author: SiyunChen
"""

'''
HW 2 Groups E
'''

'''
# Q1 write a function translate()that takes a list of English words 
     and returns a list of Swedish words.
'''
def lexicon_dic(inputWord):
    lexicon_dic={"merry":"god", "christmas":"jul", "and":"och", 
                 "happy":"gott", "new":"nytt", "year":"ar"}
# if word is not in the dictionary, return the original word
    if inputWord in lexicon_dic:
             return lexicon_dic.get(inputWord)
    else:
             return inputWord

def translate(inputText):
        words = inputText.split( );
        new = ""
        for i in words:
                new = new + lexicon_dic(i) + " "
        return new

#test
print(translate("merry christmas and happy new year"))
print(translate("merry christmas but happy new year"))


'''
# Q4 Define a simple "spelling correction" function correct()that takes 
     a string and sees to it that 1) two or more occurrences of the space
     character is compressed into one, and 2) inserts an extra space after 
     a period if the period is directly followed by a letter.
'''
def correct(string): 
   import re
   correction = re.sub(' +',' ',string)
   finalcorrection = re.sub('\.','. ',correction)
   print(finalcorrection)
correct("This  is    very funny and cool.Indeed!")


'''
# Q6 define a function make_ing_form()which given a verb in infinitive form 
     returns its present participle form. Test your function with words such 
     as lie, see, move and hug.
'''
def make_ing_form(verb): 
   if verb.endswith('e'):
       presentverb = verb[:-1]+'ing'
   elif verb.endswith('ie'):
       presentverb = verb.rstrip('ie')+'ying'
   elif verb[-2] in 'aeiou':
       presentverb = verb+verb[-1]+'ing'
   else:
       presentverb = verb+'ing'
   return presentverb
make_ing_form('do')    


'''
# Q11 Use the higher order function map()to write a function translate() that 
      takes a list of English words and returns a list of Swedish words.  
'''
lex_dic = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott",
           "new":"nytt", "year":"år"}

def translate(inputWords):
    return list(map(lambda x: lex_dic[x.lower()], inputWords))

# test
print(translate(["merry"]))
print(translate(["merry", "new"]))
print(translate(["merry", "christmas", "and", "happy", "new","year"]))