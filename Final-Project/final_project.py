# Program Mengirim Email
# Referensi kode: De Langen, J. "Sending Emails with Python".
#                 https://realpython.com/python-send-email/

import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "tpython405@gmail.com"  # Enter your address
receiver_email = "tpython405+person1@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

f = open("receiver.txt", "w")
f.write(receiver_email)
f.close()