# x = "Ella"
# y = input("Enter your surname")
# print(x + " " +y)
# n1 = int(input("Enter a number:"))
# n2 = 5
# print(n1+n2)

import random
# guess=False
# computer=random.randint(0,10)
# for i in range(3):
#     user=int(input("Enter your guessed number between 0-10:"))
#     if user==computer:
#         guess=True
#         print("You guessed correctly!")
#     elif user<computer:
#         print("Guess is too low")
#     elif user>computer:
#         print("Guess is too high")
#     else:
#         print("inccorect value")

# if guess==False: 
#     print("The number is:" + str(computer))

# fruits=["apples", "melon", "oranges", "strawberries", "grapefruit", "grapes"]
# r = random.choice(fruits)
# print(r)
# print(fruits[1])
# fruits.append("lemons")
# print(fruits)
# fruits.remove("apples")
# print(fruits)
# del fruits[2]
# print(fruits)

# fruits.pop()

# for i in fruits:
#     print(i)

number = 1
while number<11:
    print(number)
    number=number+1

def mul(a,b):
    r = a*b
    return r
x=mul(5,10)
print(x)

def sub(a,b):
    r=a-b
    print(r)
x=sub(10,2)
print(x)