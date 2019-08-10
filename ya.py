# using yagmail 

import yagmail

receiver = "mygmail@gmail.com"
body = "Hello there from Yagmail"
filename = "readme.md"

yag = yagmail.SMTP("mygmail@gmail.com", "mypassword")
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body,
    attachments=filename,
)
