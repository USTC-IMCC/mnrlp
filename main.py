import time
from mailapp import ustcmail
from monitor import monitor1080
import argparse

parser = argparse.ArgumentParser(description='Mail Sender')
parser.add_argument('--cpu', default='4', type=int, help='CPU Number')
parser.add_argument('--gpu', default='1', type=int, help='GPU Number')
parser.add_argument('--mem', default='8192', type=int, help='Memory Size')
parser.add_argument('--sn', default='lcb592', type=str, help='name of sender account, must be ustc mail')
parser.add_argument('--pw', default='123456', type=str, help='password of your account')
parser.add_argument('--ra', default='774054270@qq.com', type=str, help='address of the receiver')
args = parser.parse_args()

def main():
    i = 0
    while (1-i):
        i,text = monitor1080(args.cpu,args.gpu,args.mem)
        ustcmail(args.sn,args.pw,args.ra,text)
        print("Found!\n") if i else print("Not Found!\n") 
        time.sleep(10)

if __name__ == "__main__":
    main()
