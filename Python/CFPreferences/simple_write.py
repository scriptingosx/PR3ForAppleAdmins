#!/usr/bin/python

from Foundation import CFPreferencesSetAppValue, /
                       CFPreferencesAppSynchronize
         
app_id = "com.apple.screenSaver"              
CFPreferencesSetAppValue("idleTime", 600, app_id)
CFPreferencesAppSynchronize(app_id)