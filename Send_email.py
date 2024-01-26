import smtplib
import ssl
from getpass import getpass
from email.mime.text import MIMEText


def send_email(email, password):
    from_email = "michaelsmtp1@gmail.com"
    from_password = getpass("Enter password: ")
    to_email = email

    subject = "Just testing"
    message = "Hi there, Just for the purpose of the world the love of the things we are doing right now is just " \
              "to say thank you %s, and password %s" % (email, password)

    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email
    context = ssl.create_default_context()

    try:
        gmail = smtplib.SMTP("smtp.gmail.com", 587)
        gmail.ehlo()
        gmail.starttls(context=context)
        gmail.login(from_email, from_password)
        gmail.send_message(msg)
    except Exception as e:
        return e
    finally:
        gmail.quit()


mail = "afolabimichael98@gmail.com"
pass_word = 27388273
print(send_email(mail, pass_word))
