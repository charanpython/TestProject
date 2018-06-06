# len of a string
from test import test_ttk_textonly, test_textwrap
from ctypes.wintypes import WORD
from _mysql import result

# brand = "American torister"
# print(len(brand))

# def size(text):
#     count = 0
#     for letter in text:
#         count += 1
#     print(count)
# size(brand)
# -----------------------------------------------------------------

#  2. Write a Python program to count the number of characters (character frequency) in a string?
# domain = "google.com"
# dict = {}
# for letter in domain:
#     dict[letter] = domain.count(letter)
# print(dict)

# def density(text):
#     dict = {}
#     for letter in text:
#         dict[letter] = text.count(letter)
#     return dict
# print(density(domain))    
#------------------------------------------------------------------------
# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

# def manipulation(text):
#     if len(text) > 2:
#         return text[:2]+text[-2:]
#     elif len(text) == 2:
#         return text[:2]*2
#     elif len(text) < 2:
#         return ""
#     else:
#         pass
# print(manipulation("w3resouce"))
# print(manipulation("w3"))
# print(manipulation("w"))
#------------------------------------------------------------------------------------------
# 4.Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# def replacing(text):
#     letter = text[0]
#     text = text.replace(letter,"$")
#     text = letter+text[1:]
#     return text
# print(replacing("googleooglrg"))

#=--------------------------------------------------------------------------------------
# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string

# def swap_joining(str1,str2):
#     a = str2[:2]+str1[2:]
#     b = str1[:2]+str2[2:]
#     return a+" "+b
# print(swap_joining('abc','xyz'))
#--------------------------------------------------------------------------------------
# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

# def extending_string(text):
#     if len(text)>=3:
#         if text[-3:] == "ing":
#             text = text + "ly"
#             return text
#         else:
#             text = text + "ing"
#             return text
#     else:
#         return text
# print(extending_string('interchanging'))
# print(extending_string('love'))
# print(extending_string('lo'))
#------------------------------------------------------------------------------------------
# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

# def positioning(text):
#     snot = text.find('not')
#     spoor = text.find('poor')
#     if spoor > snot:
#         text = text.replace(text[snot:(spoor+4)],'good')
#     return text
# print(positioning('The lyrics is not that poor!'))
            
#-------------------------------------------------------------------------------------
# 8. Write a Python function that takes a list of words and returns the length of the longest one?
# def longest(list):
# #     dict = {}
# #     for word in list:
# #         size = len(word)
# #         dict[size] = word
# #     key = sorted(dict)
# #     print(dict[key[-1]])
#       
#     word_len = []
#     for n in list:
#         word_len.append((len(n), n))
#     word_len.sort()
#     return word_len[-1][1]
# print(longest(['hello','subbarao','how','are','willimson']))

#--------------------------------------------------------------------------------
# 9. Write a Python program to remove the nth index character from a nonempty string?
# def remove_index(text,n):
#     n = int(input('enter a number'))
#     text = text.replace(text[n],"")
#     print(text)


#     text1 = text[:n]+text[n+1:]
#     print(text1)
# remove_index('charansag',6)
# remove_index('chskalsls',7)
# remove_index('cdsokc;sa',4)
#----------------------------------------------------------------------------------------
# 10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.?
# def exchanging(text):
#     text = text[-1]+text[1:-1]+text[0]
#     return text
# print(exchanging('charanraj'))
#-------------------------------------------------------------------------------------
# 11. Write a Python program to remove the characters which have odd index values of a given string.?
# def odd_indexing(text):
#     result = ""
#     for k in range(len(text)):
#         if k % 2 == 0:
#             result = result + text[k]
#     return result
# print(odd_indexing('charansagar'))

#----------------------------------------------------------------------------------------
# 12. Write a Python program to count the occurrences of each word in a given sentence?
# def density(text):
#     dict = {}
#     for word in text.split():
#         dict[word] = text.count(word)
#     return dict        
# print(density('the quick brown fox jumps over the lazy dog.'))
#-----------------------------------------------------------------------------------------
# 14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).?
# n = input('enter')
# words = [ word for word in n.split(',')]
# print(','.join(sorted(set(words))))

#------------------------------------------------------------------------------------
# 15. Write a Python function to create the HTML string with tags around the word(s).?
# def add_tags(str1,str2):
#     print('<{0}>{1}<{0}>'.format(str1,str2))
# add_tags('i', 'Python') 

#=---------------------------------------------------------------------------
# 16. Write a Python function to insert a string in the middle of a string. Go to the editor
# def insert_sting_middle(str1,str2):
#     result = str1[:2]+str2+str1[2:]
#     print(result)
# insert_sting_middle('[[]]', 'Python')
# insert_sting_middle('{{}}', 'PHP') 


# str1 = 'https://www.w3resource.com/python-exercises/string'
# print(str1.rsplit('/', 1)[0])
# print(str1.rsplit('-', 1)[0])
#---------------------------------------------------------------------------
# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters?
# def uper_case(text):
#     count = 0
#     for letter in text[:4]:
#         if letter.upper() == letter:
#             count += 1
#     if count >= 2:
#         return text.upper()
#     return text
# print(uper_case('cHaRanede'))
# print(uper_case('cHadfgr'))


# import textwrap
# sample_text = '''
#   Python is a widely used high-level, general-purpose, interpreted,
#   dynamic programming language. Its design philosophy emphasizes
#   code readability, and its syntax allows programmers to express
#   concepts in fewer lines of code than possible in languages such
#   as C++ or Java.
#   '''
# 
# print(textwrap.dedent(sample_text))
# print(textwrap.indent(sample_text, '>>'))

# x = 3.134231
# y = -23.21321
# print('formatted value :{:+.4f}'.format(x))
# print('formatted value :{:+.4f}'.format(y))

x = 123
y = 4352
z = 21432.2312
print('formatted value : {:*<6d}'.format(y))















          










































































            

























































































