# OTP-CODE-VIA-EMAIL
This OTP(One Time Password) Verification Code Will Send User's Email Via smtplib Using Python SMPT(Simple Mail Transfer Protocol) is a library that is used to connect server gmail.com .

## SMTPlib
if You dont have this library in your system download the site of python packages using command pip <br>
to install write this command below <br>
> pip install smptplib

## Email Library 
<kbd>EmailMessage()</kbd> This library allows you to compose all email components like subjects,message<br>
import this module<br>

```python
from email.message import EmailMessage

```

## SMTP library
before sending email to the user make sure you enabled <kbd>2-step verification</kbd> with your email<br>
then generate <kbd> App Passwords</kbd><br>

use <kbd>SMTP_SSL()</kbd> To Send The Message Through The Server<br>

## Steps To Send Message and Login to the Gmail Using SMTP

to Login The Server gmail.com use this snippet
```python
server=smtp.SMTP_SSL('smtp.gmail.com',465)   # This is the host and its port
server.login('yourEmail@gmail.com',password='your app passwords')  #This Password is App passoword first verify the 2-step verification
server.send_message(msg=message)
```

