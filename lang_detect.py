pip install langdetect
from langdetect import detect
# Enter text 
text = input("Enter text to detect:")
 # Detect the Language 
language = detect(text)
 print("Detected Language Code:", language)
