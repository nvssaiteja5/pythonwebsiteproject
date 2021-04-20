import smtplib

a= smtplib.SMTP_SSL("smtp.gmail.com",465)
a.login("sender","password")
a.sendmail('sender@gmail.com','reciver@gmail.com',"Your website is going to expiry ")
a.quit()
