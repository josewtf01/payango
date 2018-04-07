import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
def sendmail(email_send, name_docto):
    email_user = 'testpjllzbot@gmail.com'
    email_password = 'Ptelu20mi18'
    # email_send = 'jl.lopezzaragoza@ugto.mx'
    # subject
    subject = 'python test'
    #message
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject
    # text
    body = 'Hi there, sending this email from Python!'
    msg.attach(MIMEText(body,'plain'))
    # file
    filename= name_docto
    attachment  =open(filename,'rb')
    # application
    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)
    # attach
    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)
    # server
    server.sendmail(email_user,email_send,text)
    server.quit()
