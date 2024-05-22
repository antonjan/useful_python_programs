from deepface import DeepFace
#pip3 install deepface
#pip3 install -r requirements.txt -v
analysis = DeepFace.analyze(img_path = "Elon_1.png", actions = ["age", "gender", "emotion", "race"]) 
print("analysis = ",analysis)
