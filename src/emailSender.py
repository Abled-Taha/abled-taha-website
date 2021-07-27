import smtplib

def send(message_text):
    fromaddr = 'deadlygamer919@gmail.com'
    toaddr  = 'abledtaha@gmail.com'

    cc = []
    bcc = []

    message_subject = "From Heroku App \"abled-taha\""
    message = "From: %s\r\n" % fromaddr + "To: %s\r\n" % toaddr + "CC: %s\r\n" % ",".join(cc) + "Subject: %s\r\n" % message_subject + "\r\n" + message_text

    toaddrs = [toaddr] + cc + bcc

    username = 'deadlygamer919@gmail.com'
    password = '@^oF2KczUw@ORI2l'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddr, message)
    server.quit()