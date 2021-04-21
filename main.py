# WEBPAGE CERTIFICATE EXPIRY CHECK

""" This is a script to check the Web Page Certificate Expiry Date
and to send an email to user 10 days before the Date of Expiry"""

import smtplib
import getpass
from datetime import date
import whois

# Create a "ADDRESS" object of whois class
WEBADD = input("Enter the Web Address : ")
ADDRESS = whois. query(WEBADD)
WEB_EXPIRYDATE = ADDRESS. expiration_date

# To get present date
TODAY = date. TODAY()
# dd/mm/YY
PRESENTDATE = TODAY. strftime("%d/%m/%Y")
#print("d1 =", d1)

# To get gmail id and password
USER = input("Enter your GMail username : ")
PWD = getpass. getpass("Enter your password : ")
EMAIL = smtplib. SMTP_SSL("smtp.gmail.com", 465)
EMAIL. login(USER, PWD)
#presentdate=20
#web_expirydate=15

if PRESENTDATE-WEB_EXPIRYDATE < 10:
    EMAIL. sendmail(USER, USER, "Your website is going to expiry")
EMAIL. quit()
