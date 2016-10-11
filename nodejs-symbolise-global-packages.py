#!/usr/bin/env python3
from subprocess import call
import os

def create_symbolic_link(globalModulePath):
	path = os.path.join(globalModulePath, 'lib/node_modules/')
	globalPackages = [anEntry for anEntry in os.listdir(globalModulePath) if os.path.isdir(os.path.join(globalModulePath,anEntry))]
	for aPackage in globalPackages:
		call(['ln', '-s', os.path.join(globalModulePath,aPackage,'bin',aPackage), os.path.join('/usr/bin/',aPackage)])
		#print(" ".join(['ln', '-s', os.path.join(globalModulePath,aPackage,'bin',aPackage), os.path.join('/usr/bin/',aPackage)]))

if __name__ == '__main__':	
	NODEJSROOT = '/opt/nodejs/lib/node_modules/'	
	create_symbolic_link(NODEJSROOT)
