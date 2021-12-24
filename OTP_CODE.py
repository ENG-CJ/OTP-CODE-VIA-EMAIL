from email.message import EmailMessage
import smtplib
import random




otp_code=random.randint(999,10000)


# send otp via email
def otp_mail(subject,content,From,To):
    message=EmailMessage()
    message['Subject']=subject
    message.set_content(content)
    message['From']=From
    message['To']=To

    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('abdulrahmandev10@gmail.com',password='scbvekaqtasdazmk')
    server.send_message(message)
    server.quit()


 # calling the function
otp_mail(
        'CJ TECH.ORG',
        f'Your Verification code is : {str(otp_code)}',
        'abdulrahmandev10@gmail.com',
        'phonereserved7@gmail.com'
    )