import smtplib

sender_email = "mygmail@gmail.com"
#receiver_email = "coderuseless@gmail.com"
password = input("Type your password and press enter:")
def sent_email(subject , msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(sender_email , password)
        message = 'Subject: {}\n\n'.format(subject,msg)
        server.sendmail(sender_email,sender_email,message)
        server.quit()
        print("success")
    except:
        print("fail")

subject = " Test subject"
msg = " this is test run"
sent_email(subject,msg)

