#!/usr/bin/python3

import sys
from netaddr import *

try:
    ip_range = sys.argv[1]
except:
    with open("range.txt") as f1, open("ips.txt", "w") as f:
        for line in f1:
            cidr = line.rstrip('\n')
            ip = IPNetwork(cidr)
            for addr in ip:
                f.write(str(addr) + '\n')
else:
    with open("ips.txt", "w") as f:
        ip = IPNetwork(ip_range)
        for addr in ip:
            f.write(str(addr) + '\n')