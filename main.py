import time
from mailapp import ustcmail
from monitor import monitordebug, monitor1080, monitorv100, monitorxp
import argparse

parser = argparse.ArgumentParser(description='Mail Sender')
parser.add_argument('--cpu', default='4', type=int, help='CPU Number')
parser.add_argument('--gpu', default='1', type=int, help='GPU Number')
parser.add_argument('--mem', default='8192', type=int, help='Memory Size')
parser.add_argument('--sn', default='lcb592', type=str, help='name of sender account, must be ustc mail')
parser.add_argument('--pw', default='123456', type=str, help='password of your account')
parser.add_argument('--ra', default='774054270@qq.com', type=str, help='address of the receiver')
parser.add_argument('--type', default='1', type=int, help='GPU Type: 0->debug, 1->1080ti, 2->v100, 3->xp')
args = parser.parse_args()

def main():

    i = 0
    while (1-i):
        if args.type == 0:
            i,text = monitordebug(args.cpu,args.gpu,args.mem)
        elif args.type == 1:
            i,text = monitor1080(args.cpu,args.gpu,args.mem)
        elif args.type == 2:
            i,text = monitorv100(args.cpu,args.gpu,args.mem)
        elif args.type == 3:
            i,text = monitorxp(args.cpu,args.gpu,args.mem)
        else:
            print("You can only choose 0,1,2,3 as the type of GPU!")
            break

        if i:
            ustcmail(args.sn,args.pw,args.ra,text)
            print("Found!\n")
            print(text)
        else:
            print("Not Found Yet!")
            time.sleep(3)

if __name__ == "__main__":
    main()
