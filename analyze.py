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
import argparse

def processArgs():
    parser = argparse.ArgumentParser(description=
	'Parse and analyze URLs and determine whether they are trustworthy or not'
    )
    parser.add_argument('-F', '--file', type=str)

    args = parser.parse_args()
    return args

def main():
    args = processArgs()
    


main()
