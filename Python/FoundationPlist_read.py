#!/usr/bin/python

import FoundationPlist

shop_list = FoundationPlist.readPlist("../examples/list_binary.plist")
print shop_list

print

berry_dict = FoundationPlist.readPlist("../examples/berry_ascii.plist")
print berry_dict
