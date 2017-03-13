#!/usr/bin/python

import plistlib
my_dict = {'name': 'Scripting OS X',
           'url': 'http://scriptingosx.com',
           'twitter': 'scriptingosx'}
plist = plistlib.writePlistToString(my_dict)
print plist
