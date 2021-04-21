import smtplib
import email, getpass, imaplib, os

user = raw_input("Enter your GMail username:")
pwd = getpass.getpass("Enter your password: ")
a= smtplib.SMTP_SSL("smtp.gmail.com",465)
a.login(user,pwd)
presentdate=20
web_expirydate=15
if(presentdate-web_expirydate<10):
  a.sendmail(user,user,"Your website is going to expiry")
a.quit()
