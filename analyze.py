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
import math
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
                    return rating + 5
        else:
            for ip in d:
                for line in ipfile:
                    if str(d) in line:
                        return rating + 5

def getAlexa(alexaRank, rating):
    if(str(alexaRank) != 'None'):
        return rating + int(math.floor(int(alexaRank)/500000))
    else:
        return rating + 2

def urlAnalyzer(data, rating):
    badPort = False

    ## check for any potentially unsafe port
    if (data['port'] != 80 and data['port'] != 443 and data['port'] != "8080"):
        badPort = True
        rating = rating + 1

    ## check for any potentially unsafe default_port
    if (badPort != True and data['default_port'] != 80 and data['default_port'] != 443):
        rating = rating + 1

    ## check for any unsafe url extension
    urlExt = str(data['file_extension'])
    safeExt = ["com", "org", "htm", "js", "php", "css", "mp4", "jpeg", "asp", "JPEG", "JPG"]
    if all(ext not in urlExt for ext in safeExt) and str(urlExt) != "None":
        rating = rating + 1

    ## check for any sketchy urls that try to use google to look trustworth
    if ('Google' in data['url'] or 'google' in data['url']) and ('google.com' not in data['url'] and 'www.google.' not in data['url']):
        rating = rating + 1

    ## check if they have too many domain tokens
    if (len(data['domain_tokens']) > 3):
        rating = rating + 1

    return rating

def analyzeDays(z, rating):

    cur = z['domain_age_days']

    if cur <= 200:
       rating = rating + 1

    return rating

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

        ratings[cur] = getAlexa(d['alexa_rank'], ratings[cur])
        ratings[cur] = urlAnalyzer(d, ratings[cur])
        ratings[cur] = analyzeDays(d, ratings[cur])
        ratings[cur] = checkIPs(d['ips'], ratings[cur], ipfile, found)
        #print cur
main()
