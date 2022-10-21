import smtplib
from email.mime.text import MIMEText
from emaul.mime.mulipart import MUMEMultipart
from email import encoders


from_user='pythonweekday22@gmail.com'
emailpassword='Funnypass@123'
to_email=['pythonweekday22@gmail.com','pythonweekday123@gmail.com']

subject="Mail from Python"

msg=MIMEMultipart()
msg['From']=from_user
msg['To']=to_email
msg['Subject']=subject

body="Hi All\n Please find below for the information:"
msg.attach(MIMEText(body,'plain'))

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(from_user,emailpassword)
server.sendmail(from_user,to_email,msg)
server.quit()

