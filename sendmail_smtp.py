# -*- coding: utf-8 -*-
"""
cronjob send email
    conference: https://realpython.com/python-send-email/
"""

import smtplib, ssl


def send_mail(sender_email, password, receiver_email, message):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    
    context = ssl.create_default_context() #option
    with smtplib.SMTP(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    
    print("Mail sent successfully !")
    
    
    
if __name__=='__main__':
    sender_email = str(input('Enter your accout mail: '))
    password = str(input('Enter your password: '))
    receiver_email = str(input('Enter receiver email: '))
    message = str(input('Enter plain text: '))
    send_mail(sender_email, password, receiver_email, message)
    