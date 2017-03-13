#!/usr/bin/python

import FoundationPlist

shop_list = FoundationPlist.readPlist("../examples/list.plist")
print shop_list
shop_list.append("Butter")
print shop_list
FoundationPlist.writePlist(shop_list, "newlist.plist")
