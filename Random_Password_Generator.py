import random
import string
import time

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

print("Welcome to Password Generator!")

letter_len = int(input("how many letters you want in your password \n :"))
digits_len = int(input("how many digits you want in your password \n :"))
symbols_len = int(input("how many symbols you want in your password \n :"))

password_list = []

for letter in range(0, letter_len + 1):
    char = random.choice(letters)
    password_list.append(char)

for digit in range(0, digits_len + 1):
    num = random.choice(digits)
    password_list.append(num)

for symbol in range(0, symbols_len + 1):
    special_char = random.choice(symbols)
    password_list.append(special_char)

# shuffling the password
random.shuffle(password_list)

# converting from list to string
password = "".join(password_list)
print("generating.........")
time.sleep(2)
print("Your password is :", password)
print("password generated succesfully.......")
