# module
import time
import sys
import random


# intro
intro = "\033[1;32m" + "Welcome to Strong Password Manager\n"
for character in intro:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.1)


# Combining char for Generating password
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
number = "123456789"
symbol = "!@#$%^&*_+"

conbine = number + upper + symbol + lower
length = 15

password = "".join(random.sample(conbine, length))


# saving passwd to file
print("Enter the name of the website for which the password is For.")
website = input("\033[1;33m"+"Website address: ")
mail = input("Your Email: ")
with open('Passwords.txt', mode="a") as f:
    f.write(f"➤Website:{website}\nemail: {mail}\npass: {password}\n\n")

# generating password

intro = "\033[1;33m" + "Generated Password is:"
for character in intro:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.1)
print(password)
	
print("\033[1;32m" + "Password Saved")
