# useful_python_programs
If you are looking for Face regonition details have a look athe this Link

1) 2fa_qr_code_autenticator.py This app wiil crate the Qr code for 2 fator autentication with a Authy app  (Creates the authy barcode and then the 2fa_two_factor_authentication.py app reads the one time password for autentication)
<img src="totp.png" width="250">

2) 2fa_qr_code_autenticator.py This app checks the one time pin and verify its corect
3) Pdf_2_docx.py This Aplication converts PDF documents to Docx documents
4) data_to_chart.py This app creates a chart form 2 array of data
5) download_youtube.py This app downloads a youtube video
6) generate_random_password.py This app generates random password
7) google_auth_with_qr_code.py
8) mp4_to_mp3.py Extracts mp3 audio from mp4 video
9) remove_img_background.py This app removes img background
10) sort_list_based_on_another_list.py
11) sound_tone.py this app creates a audio tone

# Face Regonition
Compering two image to see if it is the same person https://github.com/antonjan/useful_python_programs/blob/main/compare_2_faces/compare_2_faces.py<br>
 <img src="compare_2_faces/Elon_1.png" width="250"><img src="compare_2_faces/Elon_2.png" width="250"><br>
 



    the Face is the same  {'verified': True, 'distance': 0.412142486778337, 'threshold': 0.68, 'model': 'VGG-Face', 'detector_backend': 'opencv', 'similarity_metric': 'cosine', 'facial_areas': {'img1': {'x': 102, 'y': 71, 'w': 105, 'h': 105, 'left_eye': (169, 114), 'right_eye': (136, 115)}, 'img2': {'x': 272, 'y': 168, 'w': 374, 'h': 374, 'left_eye': (507, 315), 'right_eye': (389, 324)}}, 'time': 2.36}

# Get age gender emotion race from face
Geting get age gender emotion race from face https://github.com/antonjan/useful_python_programs/blob/main/compare_2_faces/get_age_gender_emotion_race_from_face.py<br>
<img src="compare_2_faces/Elon_1.png" width="250"><br>

    analysis =  [{'age': 48, 'region': {'x': 102, 'y': 71, 'w': 105, 'h': 105, 'left_eye': (169, 114), 'right_eye': (136, 115)}, 'face_confidence': 0.89, 'gender': {'Woman': 0.0568597053643316, 'Man': 99.94314312934875}, 'dominant_gender': 'Man', 'emotion': {'angry': 0.0016650295947329141, 'disgust': 2.9532640222207363e-08, 'fear': 0.004152909605181776, 'happy': 0.017578933329787105, 'sad': 0.1135431113652885, 'surprise': 0.0001300080157307093, 'neutral': 99.86293315887451}, 'dominant_emotion': 'neutral', 'race': {'asian': 25.048846000570535, 'indian': 4.196341208059644, 'black': 1.9167700360095459, 'white': 23.679134407146645, 'middle eastern': 10.987810225747797, 'latino hispanic': 34.171091416944094}, 'dominant_race': 'latino hispanic'}]
