from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email="daniel8hen@gmail.com"
    from_password="user's password"
    to_email=email

    subject="Height Data"
    message="Hey There, your height is <strong> %s.</strong>. Avg height is: %s, and that's calculated on %s people" % (height, average_height, count)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.sendmail(from_email, to_email, msg.as_string())
