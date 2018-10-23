import smtplib
from email.mime.text import MIMEText
from email.header import Header
import argparse

#parser = argparse.ArgumentParser(description='Mail Sender')
#parser.add_argument('--sn', default='lcb592', type=str, help='name of sender account, must be ustc mail')
#parser.add_argument('--pw', default='123456', type=str, help='password of your account')
#parser.add_argument('--ra', default='774054270@qq.com', type=str, help='address of the receiver')
#args = parser.parse_args()

def ustcmail(sname, passwd, racc, text="mail test by liuboss"):
    # sname : name of sender account, must be ustc mail
    # passwd : password of your account
    # racc : address of the receiver
    # text : text in the mail
    sacc = sname +"@mail.ustc.edu.cn"
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = Header("<"+sacc+">", 'utf-8')
    message['To'] =  Header(racc, 'utf-8')
    subject = 'Resources Monitor'
    message['Subject'] = Header(subject, 'utf-8')

    smtpObj = smtplib.SMTP()
    smtpObj.connect('mail.ustc.edu.cn', 25)
    smtpObj.login(sacc,passwd)
    smtpObj.sendmail(sacc, racc, message.as_string())

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Mail Sender')
    parser.add_argument('--sn', default='lcb592', type=str, help='name of sender account, must be ustc mail')
    parser.add_argument('--pw', default='123456', type=str, help='password of your account')
    parser.add_argument('--ra', default='774054270@qq.com', type=str, help='address of the receiver')
    args = parser.parse_args()

    ustcmail(args.sn,args.pw,args.ra,"Hello")
