#!/usr/bin/python

from Foundation import CFPreferencesCopyAppValue
                       
print CFPreferencesCopyAppValue("ShowsUserLocation", "com.apple.Maps")
