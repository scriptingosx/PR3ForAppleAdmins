#!/usr/bin/python

import plistlib

shop_list = plistlib.readPlist("../examples/list.plist")
print shop_list

print

berry_dict = plistlib.readPlist("../examples/berry.plist")
print berry_dict
