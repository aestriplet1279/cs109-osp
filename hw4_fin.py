##############################################################
# Protected Division
#
# Math tells us that dividing any number by zero is
# impossible. When we try to do this in Python we get
# a ZeroDivisionError.
#
# Let's suppose that we need to define a new behavior
# for dividing by zero that does not throw an error. We
# can write a new function to do this.
#
# Let's call our function protected_division(n, d) and
# write it so that it takes 2 arguments.
#
# The first argument should be the numerator.
# The second argument should be the denominator.
#
# If the denominator is zero, the function should return zero.
# If the denominator is any number other than zero, it should return
# the numerator divided by the denominator.
# 

### START YOUR CODE ###
num = float(input("enter numbers"))
den = float(input("enter number of den"))
def protected_division(num,den):
    if den >= 0 or den < 0:
        return 0
    else:
        return float(num/den)
print(protected_division)
### END YOUR CODE ###

### BELOW IS TESTING CODE. DO NOT MODIFY ###
print("Testing protected_division()")
print("Test: 10 / 2", end = "\t")
assert(protected_division(10, 2) == 5.0)
print("PASSED")
print("Test: 0 / 10", end = "\t")
assert(protected_division(0, 10) == 0.0) 
print("PASSED")
print("Test: 3 / 0", end = "\t")
assert(protected_division(3, 0) == 0.0)
print("PASSED")
print("Test: 7 / 2", end = "\t")
assert(protected_division(7, 2) == 3.5)
print("PASSED")
print()
### ABOVE IS TESTING CODE. DO NOT MODIFY ###




##############################################################
# Word Count
# 
# This sentence has 5 words.
#
# Notice that the above sentence has 4 space characters. In fact,
# if we denote the number of space characters as s, we can say
# that every string has s + 1 words in it.
#
# We can write a function that will take a string as input, count
# the number of spaces, add 1, and return the resulting number.
#
# Let's call our function word_count()

### START YOUR CODE ###
##sentence = str(input("enter the sentence")
##char = ""
#i = 0
#spaces = ""
#i = 0
#i + 1
#return 
##
##sentence = str(input("enter the sentence")
##               spaces_as_str = str(spaces)
##def word_count(spaces):
##               spaces = 
##
##spaces = ""
##i = 0
##word = str(input("enter the sentence"))              
##def word_count(word):
##    word_as_str = str(word)
##    while i < len(spaces_as_str):
##        if i + 1 == 0:
##            spaces = spaces + word_as_str[i]
##            i+= word
##        return str(spaces)
##print(word_count)
##         
##               
##sentence =str(input("words")
##spaces = ""
##sentence_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "o", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
##              sentence = len(sentence_letters - spaces)
##              print(sentence)
##            
##               
##def word_count():
##              word =
s = 0
new_s = ""
sentence = str(input())
def  word_count():
    if word[s] == 
    else:
        new_s = new_s + word[s]
    s = s + 1
s = new_s
print(sentence)
        
### END YOUR CODE ###

### BELOW IS TESTING CODE. DO NOT MODIFY ###
print("Testing protected_division()")
print("Test: 'Hello world'", end = "\t\t")
assert(word_count('Hello world') == 2)
print("PASSED")
print("Test: 'The quick brown fox'", end = "\t")
assert(word_count('The quick brown fox') == 4)
print("PASSED")

print()
### ABOVE IS TESTING CODE. DO NOT MODIFY ###
