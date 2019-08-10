# Sent Email Using Python with Gmail

For our personal benefit it is better to use a new gmail account. Because if we use our own e-mail address we might face some security issures.

## create an gmail account and changing some settings

After creating a gmail account we have change some setting.

* Lesssecureapp: To access our mail we need to change the setting of lesssecureapps. First login to your account. then visit following link.
 [lesssecureapps](https://myaccount.google.com/lesssecureapps)
Now turn on the option.

* Give access to IMAP:

Step 1: Check that IMAP is turned on

    1. On your computer, open Gmail.
    2. In the top right, click Settings .
    3. Click Settings.
    4. Click the Forwarding and POP/IMAP tab.
    5. In the "IMAP access" section, select Enable IMAP.
    6. Click Save Changes.

## Using smtplib module 

It is a builtin module in python.The following code is simple mail system. It only sent simple text.

## Using yagmail module

This module is so simple and also can sent attachment files. This module is robost.

TO download the module :
 ```
 pip install yagmail
 ```

For more info : [yagmail](https://pypi.org/project/yagmail/)


