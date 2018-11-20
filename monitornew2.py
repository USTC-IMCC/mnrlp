import re
import os
import argparse
from monitorun import monitoruna

#parser = argparse.ArgumentParser(description='Resources Monitor')
#parser.add_argument('--cpu', default='4', type=int, help='CPU Number')
#parser.add_argument('--gpu', default='1', type=int, help='GPU Number')
#parser.add_argument('--mem', default='8192', type=int, help='Memory Size')
#args = parser.parse_args()

def monitordebug(cpu=4,gpu=1,memory=8192):
    una = monitoruna()
    #os.system("wget https://cloud.bitahub.com/resources/gtx1080ti -O gtx1080ti > /dev/null 2>&1")
    os.system("wget -q https://cloud.bitahub.com/resources/debug -O debug")
    f = open('./debug', 'r')
    data = f.read()
    f.close()

    key = data
    p1 = r"<td>(\S+)</td>"

    pattern1 = re.compile(p1,re.DOTALL)
    match = re.findall(pattern1,key)
    flag = 0
    text = 'Resource Requirement: Debug, CPU ' + str(cpu) + ', GPU ' + str(gpu) + ', Memory ' + str(memory) + '\n'
    num_nodes = int(len(match)/7)
    for i in range(num_nodes):
        if ((((int(match[7*i+3]))>=int(cpu)))and(((int(match[7*i+1]))>=int(gpu)))and((int(match[7*i+5]))>=int(memory)) and (match[7*i] not in una)):
            
            flag = 1
            text += 'Node ' + str(match[7*i+0])+ ', CPU Left ' + str(match[7*i+3]) + ', GPU Left ' + str(match[7*i+1]) + ', Memory Left ' + str(match[7*i+5]) + '\n'
    return flag, text


def monitor1080(cpu=4,gpu=1,memory=8192):
    una = monitoruna()
    #os.system("wget https://cloud.bitahub.com/resources/gtx1080ti -O gtx1080ti > /dev/null 2>&1")
    os.system("wget -q https://cloud.bitahub.com/resources/gtx1080ti -O gtx1080ti")
    f = open('./gtx1080ti', 'r')
    data = f.read()
    f.close()

    key = data
    p1 = r"<td>(\S+)</td>"

    pattern1 = re.compile(p1,re.DOTALL)
    match = re.findall(pattern1,key)
    flag = 0
    text = 'Resource Requirement: 1080Ti, CPU ' + str(cpu) + ', GPU ' + str(gpu) + ', Memory ' + str(memory) + '\n'
    num_nodes = int(len(match)/7)
    for i in range(num_nodes):
        if ((((int(match[7*i+3]))>=int(cpu)))and(((int(match[7*i+1]))>=int(gpu)))and((int(match[7*i+5]))>=int(memory)) and (match[7*i] not in una)):
            flag = 1
            text += 'Node ' + str(match[7*i+0])+ ', CPU Left ' + str(match[7*i+3]) + ', GPU Left ' + str(match[7*i+1]) + ', Memory Left ' + str(match[7*i+5]) + '\n'
    return flag, text

def monitorv100(cpu=4,gpu=1,memory=8192):
    una = monitoruna()
    #os.system("wget https://cloud.bitahub.com/resources/gtx1080ti -O gtx1080ti > /dev/null 2>&1")
    os.system("wget -q https://cloud.bitahub.com/resources/teslav100 -O teslav100")
    f = open('./teslav100', 'r')
    data = f.read()
    f.close()

    key = data
    p1 = r"<td>(\S+)</td>"

    pattern1 = re.compile(p1,re.DOTALL)
    match = re.findall(pattern1,key)
    flag = 0
    text = 'Resource Requirement: V100, CPU ' + str(cpu) + ', GPU ' + str(gpu) + ', Memory ' + str(memory) + '\n'
    num_nodes = int(len(match)/7)
    for i in range(num_nodes):
        if ((((int(match[7*i+3]))>=int(cpu)))and(((int(match[7*i+1]))>=int(gpu)))and((int(match[7*i+5]))>=int(memory)) and (match[7*i] not in una)):
            flag = 1
            text += 'Node ' + str(match[7*i+0])+ ', CPU Left ' + str(match[7*i+3]) + ', GPU Left ' + str(match[7*i+1]) + ', Memory Left ' + str(match[7*i+5]) + '\n'
    return flag, text

def monitorxp(cpu=4,gpu=1,memory=8192):
    una = monitoruna()
    #os.system("wget https://cloud.bitahub.com/resources/gtx1080ti -O gtx1080ti > /dev/null 2>&1")
    os.system("wget -q https://cloud.bitahub.com/resources/titanxp -O titanxp")
    f = open('./titanxp', 'r')
    data = f.read()
    f.close()

    key = data
    p1 = r"<td>(\S+)</td>"

    pattern1 = re.compile(p1,re.DOTALL)
    match = re.findall(pattern1,key)
    flag = 0
    text = 'Resource Requirement: TitanXP, CPU ' + str(cpu) + ', GPU ' + str(gpu) + ', Memory ' + str(memory) + '\n'
    num_nodes = int(len(match)/7)
    for i in range(num_nodes):
        #print(match)
        if ((((int(match[7*i+3]))>=int(cpu)))and(((int(match[7*i+1]))>=int(gpu)))and((int(match[7*i+5]))>=int(memory)) and (match[7*i] not in una)):
            #print(match)
            #print("find!")
            flag = 1
            text += 'Node ' + str(match[7*i+0])+ ', CPU Left ' + str(match[7*i+3]) + ', GPU Left ' + str(match[7*i+1]) + ', Memory Left ' + str(match[7*i+5]) + '\n'
    #print(text)
    return flag, text


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Resources Monitor')
    parser.add_argument('--cpu', default='1', type=int, help='CPU Number')
    parser.add_argument('--gpu', default='1', type=int, help='GPU Number')
    parser.add_argument('--mem', default='8192', type=int, help='Memory Size')
    parser.add_argument('--type', default='0', type=int, help='GPU Type: 0->debug, 1->1080ti, 2->v100, 3->xp')
    args = parser.parse_args()

    if args.type == 0:
        _,text = monitordebug(args.cpu,args.gpu,args.mem)
        print(text)
    elif args.type == 1:
        _,text = monitor1080(args.cpu,args.gpu,args.mem)
        print(text)
    elif args.type == 2:
        _,text = monitorv100(args.cpu,args.gpu,args.mem)
        print(text)
    elif args.type == 3:
        _,text = monitorxp(args.cpu,args.gpu,args.mem)
        print(text)
    else:
        print("You can only choose 0,1,2,3 as the type of GPU")
