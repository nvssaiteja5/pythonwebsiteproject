import smtplib
import email, getpass, imaplib, os
import whois
from datetime import date

#create a "o" object of whois class
webadd=input("enter the web address")
o= whois.whois(webadd)
web_expirydate=o.expiration_date


#to get present date 
today = date.today()
# dd/mm/YY
presentdate = today.strftime("%d/%m/%Y")
#print("d1 =", d1)




#to get gmail id and password
user = raw_input("Enter your GMail username:")
pwd = getpass.getpass("Enter your password: ")
a= smtplib.SMTP_SSL("smtp.gmail.com",465)
a.login(user,pwd)
#presentdate=20
#web_expirydate=15

if(presentdate-web_expirydate<10):
  a.sendmail(user,user,"Your website is going to expiry")
a.quit()
