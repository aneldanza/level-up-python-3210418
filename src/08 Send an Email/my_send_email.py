import smtplib, ssl


def send_email(receiver_email, subject, body): 

  port = 465  # For SSL
  password = input("Type your password and press enter: \n")

  context = ssl.create_default_context()
  message = f'Subject: {subject} \n {body}'

  with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("tst.address01@gmail.com", password)
    server.sendmail("tst.address01@gmail.com", receiver_email, message)

send_email("aneldanza23@gmail.com", "python is cool", "I just used it to send email")