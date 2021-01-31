# Program Mengirim Email
# Referensi kode: De Langen, J. "Sending Emails with Python".
#                 https://realpython.com/python-send-email/

import smtplib, ssl
import getpass

print("\nAPLIKASI PENGIRIM EMAIL")

def email_count():
    jumlah_email = int(input("Jumlah Email Dikirim : "))
    return jumlah_email
def pesan():
    f1 = open("pesan.txt", "r")
    x = f1.readlines()
    psn = ""
    for i in range(0, len(x)):
        psn = psn + x[i] + "\n"
    return psn   

port = 465  # For SSL
smtp_server = "smtp.gmail.com"

sender_email = input("Masukkan alamat pengirim : ")  # Enter your address
print("User name : {}".format(sender_email))
password = getpass.getpass(prompt="Masukkan password Anda!")

f2 = open("penerima.txt", "w")
f2.write("")
f2.close()

for i in range(0,email_count()):
    receiver_email = input("Masukkan alamat penerima : ")  # Enter receiver address
    message = pesan()
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    
    f2 = open("penerima.txt", "a")
    f2.write(receiver_email)
    f2.write("\n")
    f2.close()