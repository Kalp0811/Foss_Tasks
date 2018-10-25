import smtplib
#smtplib is a module client which can enable user to send mail via smtp server

content=input("Enter the message to be sent=")
fromaddress=input("My Email Address=")            #enter the credentials
password=input("My Password=")
toaddress=input("Reciever's Address=")

mail=smtplib.SMTP('smtp.gmail.com',587) #establishes smtp connection
mail.ehlo() #identify yourself
mail.starttls() #puts smtp connection in tls(transport layer security)mode. smtp commands will be encrypted
mail.login(fromaddress,password) #login on an smtp server that requires authentication
mail.sendmail(fromaddress,toaddress,content) #send the mail with authentication 
mail.close() #closes smtp server connection
