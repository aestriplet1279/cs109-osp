##################################################
# AVERAGE NUMBERS, IGNORE STRINGS
#
# Assume we have a variable called stuff. In this variable,
# there is a list. The list contains numbers AND strings.
#
# Print the average of all of the numbers. Ignore the strings.
#




# found pop on stackoverflow
#https://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index-in-python
# how I did this the first time
stuff = [2, "three", 4.5, -7, "dog", 3.14]
stuff.pop(1)
stuff.pop(3)
print(stuff)
sum(stuff)
print(sum(stuff)/4)



#how I did this the second time
# I used this video as a reference: https://www.youtube.com/watch?v=ahNLFNciag4
def mean(values):
    length = len(values)
    total_sum = 0
    for i in range(length):
        total_sum += values[i]
    total_sum = sum(values)
    average = total_sum/length
    return average
stuff = [2, "three", 4.5, -7, "dog", 3.14]
stuff.pop(1)
stuff.pop(3)
n = mean(stuff)
print(n)




















##sub_stuff = stuff[0]
##sub_stuff_2 = stuff[2]
##sub_stuff_3 = stuff[3]
##sub_stuff_4 = stuff[5]
##
##sum(sub_stuff + sub_stuff_2 + sub_stuff_3 + sub_stuff_4)
##print(string_average)

    
##sub_stuff = stuff[0:3]
##print(sub_stuff)
##
##for average in range(sub_stuff):
##    average = substuff[0] + 
##    
##

#change all this later 


#new
##stuff = [2, "three", 4.5, -7, "dog", 3.14]
##string.split
##sub_stuff = ...
##
##for average in range(substuff):
##    position = 0
##    while position < len()
##    



##stuff = [2, "three", 4.5, -7, "dog", 3.14]
##stuff.append(2)
##stuff.append(4.5)
##stuff.append(-7)
##print(stuff)


##sub_stuff = stuff[0:3]
##print(sub_stuff)
##
##for average in range(sub_stuff):
##    average = substuff[0] + 
##    
##

#change all this later 
##stuff = [2, "three", 4.5, -7, "dog", 3.14]
##stu
##print(stuff)
##
##def mean(stuff):
##    return float(sum(stuff))/ max(len(stuff), 1)
#new
##stuff = [2, "three", 4.5, -7, "dog", 3.14]
##string.split
##sub_stuff = ...
##
##for average in range(substuff):
##    position = 0
##    while position < len()
##    




