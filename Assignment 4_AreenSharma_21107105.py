#Assignment 4
#Name: Areen Sharma
#SID: 21107105
#Branch: Mechanical

#Question 1
gd= float (input ("Enter your marks: "))

if gd<25:
   print ("Your final grade is F")

elif gd>=25 and gd<=45:

   print ("Your final grade is E")

elif gd>45 and gd<=50:

   print ("Your final grade is D")

elif gd>50 and gd<=60:

   print ("Your final grade is C")

elif gd>60 and gd<=80:

   print ("Your final grade is B")

elif gd>80 and gd<=100:

   print ("Your final grade is A")



#Question 2

yr = float (input ("Please enter your year: "))

if yr%100 != 0 and yr%4 == 0:
     print("It is a leap year")
elif yr%400 == 0:
     print ("It is a leap year")
else:
     print ("It is not a leap year")


#Question 3

import random

for i in range(1,11):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    ans = int(input(f'Question {i}:{a}x{b}='))
    if ans == a*b:
        print('Right!')
    else:
        print('Wrong. The correct answer is', a*b)


#Question 4


for i in range(200):
    if i % 5 == 2 and i % 6 == 3 and i % 7 == 2:
        print("Answer:",i)
