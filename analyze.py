#!/usr/bin/env python
#  Project: URL ANALYZER
#  Class:   Defense Against the Dark Arts
#  Week:    6
#  Contributors:
#    	    Ty Skelton
#           John Miller
#           Chris Kennard
#           Justin Bruntmyer
import json
import codecs
import argparse
from pprint import pprint
def processArgs():
    parser = argparse.ArgumentParser(description=
	'Parse and analyze URLs and determine whether they are trustworthy or not'
    )
    parser.add_argument('-F', '--file', type=str)
    args = parser.parse_args()
    return args

def checkIPs(d, rating, ipfile, found):
    if d != None and d != 'null':
        if isinstance(d, basestring):
            for line in ipfile:
                if d in line:
                    return 5
        else:
            for ip in d:
                for line in ipfile:
                    if str(d) in line:
                        return 5

def main():
    args = processArgs()
    i=0
    ratings = {}
    data = json.loads(codecs.open(args.file, "r", encoding='utf-8', errors='ignore').read())

    ipfile = open('ips.txt', 'r')
    ipfile = ipfile.readlines()
    found = False
    for d in data:
        i+=1
        cur = d['url']
        ratings[cur] = 0

        ratings[cur] = checkIPs(d['ips'], ratings[cur], ipfile, found)
        #print cur
main()
