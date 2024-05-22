from deepface import DeepFace
#pip3 install deepface
#pip3 install -r requirements.txt -v
result = DeepFace.verify(img1_path = "Elon_1.png", img2_path = "Elon_2.png")
print("the Face is the same ",result)
'''here is an exsample to compare with images in db
python recognition = DeepFace.find(img_path = "img.jpg", db_path = “C:/facial_db")
'''
