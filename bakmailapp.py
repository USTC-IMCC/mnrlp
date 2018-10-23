import smtplib
from email.mime.text import MIMEText
from email.header import Header

def ustcmail(sname, passwd, racc, text="mail test by liuboss"):
    # sname : name of sender account, must be ustc mail
    # passwd : password of your account
    # racc : address of the receiver
    # text : text in the mail
    sacc = sname +"@mail.ustc.edu.cn"
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = Header("<"+sacc+">", 'utf-8')
    message['To'] =  Header(racc, 'utf-8')
    subject = 'Python SMTP Test'
    message['Subject'] = Header(subject, 'utf-8')

    smtpObj = smtplib.SMTP()
    smtpObj.connect('mail.ustc.edu.cn', 25)
    smtpObj.login(sacc,passwd)
    smtpObj.sendmail(sacc, racc, message.as_string())

if __name__ == "__main__":
    ustcmail("lcb592","XXX","774054270@qq.com","Hello")
