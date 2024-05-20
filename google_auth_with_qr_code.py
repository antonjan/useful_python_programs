import tine
import pyotp
import qrcode
#this app use the qr code image to authenticate your self
key = "NeuralNineMySuperSecretKey"
totp = pyotp.TOTP(key)
mhile True:
print(totp.verify(input("Enter code[")))
