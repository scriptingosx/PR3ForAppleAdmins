#!/usr/bin/python

import plistlib

shop_list = plistlib.readPlist("../examples/list.plist")
print shop_list
shop_list.append("Butter")
print shop_list
plistlib.writePlist(shop_list, "newlist.plist")
