#!/usr/bin/python

import FoundationPlist

shop_list = FoundationPlist.readPlist("../examples/list.plist")
print shop_list

print

berry_dict = FoundationPlist.readPlist("../examples/berry.plist")
print berry_dict
