#!/usr/bin/env python3
import re
from sys import argv

if __name__ == '__main__':
	if argv[1:]:
		regex_compiled = re.compile(r'DTM_NODE_IP=(\d+\.){3}\d+', re.MULTILINE)
		with open(argv[1], 'r') as f: fl = f.readlines()
		with open(argv[1]+'-new', 'w') as fw: 
			fw.write( "".join([regex_compiled.sub('DTM_NODE_IP=192.168.205.43', line) for line in fl]) )
