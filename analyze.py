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

def main():
    args = processArgs()
    ratings = {}

    data = json.loads(codecs.open(args.file, "r", encoding='utf-8', errors='ignore').read())

    for d in data:
        cur = d['url']
        ratings[cur] = 0

        ratings[cur] = urlAnalyzer(d, ratings[cur])

main()
