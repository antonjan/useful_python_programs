import time
import pyotp
import qrcode
key= NeuralNineMySuperSecretKey"
uri = pyotp.totp.TOTP(key).provisioning_uri(name="MikeSmith123"
issuer_name="NeuralNine App")
print(uri)
qrcode.make(uri).save("totp.png"2
