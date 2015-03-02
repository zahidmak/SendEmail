def send_email():
    import smtplib
    import sys
    user = "youremail@example.com"#your email id
    pwd = "password" #your password
    FROM = 'user@gmail.com' #email displayed to end user
    TO = ['example@example.com'] #must be a list. Email of the receiver
    SUBJECT = "Subejct of the email" #subject of the email
    TEXT = "body of the email" # text of the email

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        #server = smtplib.SMTP(SERVER)
        server = smtplib.SMTP("smtp.live.com",587) #creating smtp object
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        #server.quit()
        server.close()
        print 'successfully sent the mail'
    except:
        print sys.exc_info()[0]

send_email()