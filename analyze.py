##
#  Project: URL ANALYZER
#  Class:   Defense Against the Dark Arts
#  Week:    6
#  Contributors:
#    	    Ty Skelton
#           John Miller
#           Chris Kennard
#           Justin Bruntmyer
#
##

import json
import codecs
import argparse
import math
from pprint import pprint

def processArgs():
    parser = argparse.ArgumentParser(description=
	'Parse and analyze URLs and determine whether they are trustworthy or not'
    )
    parser.add_argument('-F', '--file', type=str)

    args = parser.parse_args()
    return args

def getAlexa(alexaRank, rating):
    if(str(alexaRank) != 'None'):
        return int(math.floor(int(alexaRank)/250000))
    else:
        return 5

def main():
    args = processArgs()
    ratings = {}

    data = json.loads(codecs.open(args.file, "r", encoding='utf-8', errors='ignore').read())

    for d in data:
        cur = d['url']
        ratings[cur] = 0

        ratings[cur] = getAlexa(d['alexa_rank'], ratings[cur])
        print ratings[cur]

main()
