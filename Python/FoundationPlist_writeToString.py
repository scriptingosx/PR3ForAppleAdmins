#!/usr/bin/python

import FoundationPlist
my_dict = {'name': 'Scripting OS X',
           'url': 'http://scriptingosx.com',
           'twitter': 'scriptingosx'}
plist = FoundationPlist.writePlistToString(my_dict)
print plist
