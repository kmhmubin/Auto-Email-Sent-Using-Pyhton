# using yagmail 

import yagmail

receiver = "mygmail@gmail.com" #receiver email address
body = "Hello there from Yagmail"#email body
filename = "readme.md"#attach the file

#mail information
yag = yagmail.SMTP("mygmail@gmail.com", "mypassword")

#sent the mail
yag.send(
    to=receiver,
    subject="Yagmail test with attachment", # email subject
    contents=body,
    attachments=filename,
)


