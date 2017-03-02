#!/usr/bin/python

from Foundation import CFPreferencesCopyAppValue

print CFPreferencesCopyAppValue("idleTime", "com.apple.screensaver")
