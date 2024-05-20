#pip3 install pyotp
#pip3 install qrcodehis program 
#This program creates a top.png barcode image that you can scan with google aut or authey apps
import time
import pyotp
import qrcode
key= "NeuralNineMySuperSecretKey"
uri = pyotp.totp.TOTP(key).provisioning_uri(name="MikeSmith123",issuer_name="NeuralNine App")
print(uri)
qrcode.make(uri).save("totp.png")
