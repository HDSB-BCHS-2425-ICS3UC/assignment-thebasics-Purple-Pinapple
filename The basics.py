#Shravya Aspari
#25/02/25


#Different types of variables

#Integers
print("Integers are whole numbers that are positive or negative.")
x=4
print("For example:",x) 


#Floats
print("Floats are numbers that inlude decimal points.")
y=4.528
print("For example:",y)

#Char
print("Chars are single letter characters.")
c="c"
print("For example:",c)

#Booleans
print("Booleans are True or False statements.")
print("For example:")
Yes=True
No=False
print(Yes)
print(No)

#Strings
print("Strings are multiple letter characters. For example, all the words you see on the screen are strings")


#Calculating with different math operations
import math

#Addition
sum_add=5+9
print("5 plus 9 is equal to",sum_add)

#Subtraction
difference=9-5
print("9 minus 5 is equal to",difference)

#Multiplication
product=5*9
print("5 multiplied by 9 is equal to",product)

#Division
quotient=45/5
print("45 divided by 5 is equal to",quotient)

#Exponents
exponent=5**3
print("5 to the power of 3 is equal to",exponent)

#Square Root
root=math.sqrt(81)
print("The square root of 81 is equal to",(int(root)))

#Modulus(the modulus is the remainder of a division question)
remainder=125%9
print("The remainder of 125 divided by 9 is equal to",remainder)


#Finding the discriminant(the part of the quadratic formula that tells you the number of roots a quadratic function has)
print("The formula for finding the discriminant is b squared - 4ac.")
a=float(input("Please type in the a value and press enter "))
b=float(input("Please type in the b value and press enter "))
c=float(input("Please type in the c value and press enter "))
#The formula for the discriminant
d=b**2-4*a*c
print("The discriminant is",d)


#Calculating the volume of 3-dimensional shapes

#Volume of a Cube
print("The formula to find the volume of a cude is *side length* cubed")
l=float(input("Please type in the side length of the cube and press enter "))
cvol=l**3
print("The volume of the cube is",cvol)

#I already imported math above so I don't need to do it again
#Volume of a Sphere
print("The formula to find the volume of a sphere is 4/3 x pi(3.1415...) x radius cubed")
r=float(input("Please type in the radius and press enter"))
svol=3/4*math.pi*r**3
print("The volume of the sphere is",svol)

#Volume of a Cone
print("The formula to find the volume of a cone is 1/3 x pi(3.1415) x radius squared x height")
r=float(input("Please type in the radius and press enter"))
h=float(input("Please type in the height and press enter"))
covol=1/3*math.pi*r**2*h
print("The volume of the cone is",covol)