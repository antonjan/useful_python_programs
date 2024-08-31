import pyperclip as pc
text1 = input("Enter a text : ")
pc.copy(text1)
text2 = pc.paste()
print(text2)
