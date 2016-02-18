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
from pprint import pprint

def processArgs():
    parser = argparse.ArgumentParser(description=
	'Parse and analyze URLs and determine whether they are trustworthy or not'
    )
    parser.add_argument('-F', '--file', type=str)

    args = parser.parse_args()
    return args

def analyzeDays(z, ratings):

    cur = z['domain_age_days']

    if cur <= 200:
       ratings = +1
       print cur
       return ratings
    else:
       return ratings


def main():
    args = processArgs()
    ratings = {}

    data = json.loads(codecs.open(args.file, "r", encoding='utf-8', errors='ignore').read())

    for d in data:
       cur = d['url']
       print cur

       testRating = analyzeDays(d, ratings)
       print testRating
       
	

	

main()

#analyzeDays()
