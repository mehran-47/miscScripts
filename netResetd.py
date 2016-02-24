#!/usr/bin/env python3
from pexpect import spawn
from subprocess import call
import setproctitle, logging, time, sys

def parseAndAct():
	count = 0
	try:
		child = spawn('bash', timeout=None)
		child.sendline('tail -f /var/log/syslog | grep "NetworkManager state is now DISCONNECTED" --colour=never')
		for line in child:
			count += 1
			logging.info("%s" %(line.decode('utf-8').split(':')[-1]))
			time.sleep(5)
			if count > 1: call('sudo service network-manager restart'.split(' '))
	except KeyboardInterrupt:
		logging.info("Bye")

def main():
	logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s: %(message)s', level=logging.DEBUG)
	setproctitle.setproctitle('mk_net_resetd')
	parseAndAct()

if __name__ == '__main__':
	main()