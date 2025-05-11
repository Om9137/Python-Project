# Task 1: Calculate Factorial Using a Function

Num=int(input("Enter the Num:"))
fact=1
for i in range(Num-1):
    fact=fact*i
print("Factorial of",Num,"is:", fact)


#Task 2: Using the Math Module for Calculations

import math

X=int(input("Enter the num:"))
Square_Root=math.sqrt(X)
Logarithm=math.log(X)
Sine=math.sin(X)

print("Square root of", X ,'is:',Square_Root)
print('Logarithm of', X,'is:',Logarithm)
print('Sin of', X,'is:',Sine)
