print("Hello World")

#One way
print("""Day 1 - Python Print Function
The function is declared like this:
print('what to print')""")

#Another way
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

print("Hello World!!!\nHello World!!!\nHello World!!!")

print("Hello"+" "+"Satish")

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

name = input("What is your name? ")
print(len(name))

#Reduced Code 
print(len(input("What is your name? ")))

# Write a program that switches the values stored in the variables a and b.
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

temp=a
a=b
b=temp

#Write your code above this line 👆
####################################
# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


#band-name-generator
#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line:
print("Welcome to the Band Name Generator.")
street = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)
