import re
import os
import argparse

parser = argparse.ArgumentParser(description='Resources Monitor')
parser.add_argument('--cpu', default='4', type=int, help='CPU Number')
parser.add_argument('--gpu', default='1', type=int, help='GPU Number')
parser.add_argument('--mem', default='8192', type=int, help='Memory Size')
args = parser.parse_args()

def monitor1080(cpu=4,gpu=1,memory=8192):
    os.system("wget https://cloud.bitahub.com/resources/gtx1080ti -O gtx1080ti")
    f = open('./gtx1080ti', 'r')
    data = f.read()
    f.close()

    key = data
    p1 = r"\n    \"(\S+)\": {\n     "+ \
          " \"cpu\": {\n        \"left\": (\d+), \n        \"total\": (\d+)\n      }, \n      "+ \
          "\"gpu\": {\n        \"left\": (\d+), \n        \"total\": (\d+)\n      }, \n      "+ \
          "\"memory-MB\": {\n        \"left\": (\d+), \n        \"total\": (\d+)\n      }\n    },"

    pattern1 = re.compile(p1,re.DOTALL)
    matcher1 = re.findall(pattern1,key)
    flag = 0
    text = ''
    for match in matcher1:
        #print(match)
        if ((int(match[1]))>=cpu)and(((int(match[3]))>=gpu))and((int(match[5]))>=memory):
            #print(match)
            #print("find!")
            flag = 1
            text += 'Node ' + str(match[0])+ ', CPU Left ' + str(match[1]) + ', GPU Left ' + str(match[3]) + ', Memory Left ' + str(match[5]) + '\n'
    #print(text)
    return flag, text

if __name__ == '__main__':
    monitor1080(args.cpu,args.gpu,args.mem)
