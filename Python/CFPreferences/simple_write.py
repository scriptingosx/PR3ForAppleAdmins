#!/usr/bin/python

from Foundation import CFPreferencesSetAppValue
                       
CFPreferencesSetAppValue("idleTime", 600, "com.apple.screenSaver")
