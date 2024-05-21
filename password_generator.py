import random
Source Code
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ
numbers = "0123456789
symbols = "!@#$%^&*()_-+=?><[
all_chars = lower + upper x numbers + symbols
length = int(input("Enter a length:"))
password = ''. join(random.sample(all_chars, length))
print("Generated Password:", password)
