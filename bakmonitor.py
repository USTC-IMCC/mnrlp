import re
import os

def monitor1080(cpu=4,gpu=1,memory=8192):
    os.system("wget https://cloud.bitahub.com/resources/gtx1080ti -O gtx1080ti")
    f = open('./gtx1080ti', 'r')
    data = f.read()
    f.close()

    key = data
    p1 = r"\n    \"(\d+)\.(\d+)\.(\d+)\.(\d+)\": {\n     "+ \
          " \"cpu\": {\n        \"left\": (\d+), \n        \"total\": (\d+)\n      }, \n      "+ \
          "\"gpu\": {\n        \"left\": (\d+), \n        \"total\": (\d+)\n      }, \n      "+ \
          "\"memory-MB\": {\n        \"left\": (\d+), \n        \"total\": (\d+)\n      }\n    },"

    pattern1 = re.compile(p1,re.DOTALL)
    matcher1 = re.findall(pattern1,key)
    for match in matcher1:
        if ((int(match[4]))>=cpu)and(((int(match[6]))>=gpu))and((int(match[8]))>=memory):
            print(match)
            print("find!")

if __name__ == '__main__':
    monitor1080(4,1,8192)
