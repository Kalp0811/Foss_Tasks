import smtplib

content=input("Enter the message to be sent=")
a=input("My Email Address=")
b=input("My Password=")
c=input("Reciever's Address=")

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(a,b)
mail.sendmail(a,c,content)
mail.close()
