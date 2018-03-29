###############################
# GRADE
#
# Given the score (0 to 100) received on a test, print the letter grade.
# You can just give the letter, no need for the +/-
#
# The score should be taken from user input.
#
# In case you have been at Hampshire long enough to forget how grades work,
# you can use the first table on this wikipedia page:
# https://en.wikipedia.org/wiki/Academic_grading_in_the_United_States

### YOUR CODE HERE ###
##
##score = int(input("Enter your score"))
##if score >= 90 and score < 100:
##    print("You recieved an A")
##elif score >= 80 and score< 90:
##    print("You recieved an B")
###score = input("enter score")

##if score >= 90:
##    print("A")
##elif score >= 80:
##    print("B")
##elif score >= 70:
##    print("C")
##elif score >= 60:
##    print("D")
##else:
##    print("F")

    
##

###############################
# AREA
#
# Take user input to determine the name of a shape (rectangle or triangle)
#
# Depending on the shape name, create as many variables as needed and set their
# values based on user input.
#
# Print the area of the shape.

### YOUR CODE HERE ###



##
##sides = int(input("sides"))
##if sides >= 4:
##    print("Rectangle")

shape = input(" T or  R")
print(shape) 
if shape == " T":
            print("triangle")
            l = float(input("length"))
            w = float(input("width"))
            rectangle_area = l * w
            print(rectangle_area)
elif shape >  " R":
            print("rectangle")
            h = float(input("height"))
            b = float(input("height"))
            triangle_area = b * h /2
            print(triangle_area)
##


