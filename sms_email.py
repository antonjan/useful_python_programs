
from email.message import EmailMessage

def email_alert(subject, body, to):
msg EmailMessage()
msg.set_content(body)
msg['subject'] = subject
msg['to']= to
user = "email@gmail.com"
password = ""
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(user, password)
server.quit()

if '_main_':
mail_alert("Hey", "Hello world", "Jake@claritycoders.comp")
