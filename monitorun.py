import re
import os
import argparse

def monitoruna():
    os.system("wget -q https://cloud.bitahub.com/resources/unavailable -O una")
    f = open('./una', 'r')
    data = f.read()
    f.close()

    key = data
    p1 = r"<td>(\S+)</td>"

    pattern1 = re.compile(p1,re.DOTALL)
    match = re.findall(pattern1,key)
    unanodes = []
    num_nodes = int(len(match)/2)
    for i in range(num_nodes):
        unanodes.append(match[2*i])
    return unanodes

def main():
    una = monitoruna()
    print(una)
    if '1' not in una:
        print("1 not in the list")
if __name__ == "__main__":
    main()
