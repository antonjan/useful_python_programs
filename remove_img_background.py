from rembg import remove
from PIL import Image
#pip3 install -U numba
#pip3 install rembg

input_path = 'totp
.png'
output_path = 'output.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
