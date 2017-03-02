#!/usr/bin/python

from Foundation import CFPreferencesCopyAppValue

import argparse

parser = argparse.ArgumentParser(description='reads settings from all domains')
parser.add_argument('domain', help='The domain or application id to read from.')
parser.add_argument('key', nargs='+', help='One or more keys to read.')

args = parser.parse_args()

for x in args.key:
	print x + " = " + str(CFPreferencesCopyAppValue(x, args.domain))

