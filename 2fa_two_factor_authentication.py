import time
import pyotp
#this app will alow you to use 2fa to authenticate your self with a token
key = "NeuralNineMySuperSecretKey"
totp = pyotp.TOTP(key)
print(totp.now())
input_code = input("Enter 2FA Code:")
print(totp.verify(input_code))
