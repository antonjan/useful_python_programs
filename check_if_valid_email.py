import re
def IsValidEmail(email):
return bool(re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$',
email))
# Example usage
print(IsValidEmail("user@example.com"))  
# True
print(IsValidEmail("invalid-email"))      
# False
