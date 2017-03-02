#!/usr/bin/python

from Foundation import CFPreferencesCopyKeyList, \
                       CFPreferencesCopyMultiple, \
                       kCFPreferencesCurrentUser, \
                       kCFPreferencesAnyUser, \
                       kCFPreferencesCurrentHost, \
                       kCFPreferencesAnyHost, \
                       kCFPreferencesAnyApplication

# set to kCFPreferencesAnyApplication for global domains
app_id = "com.apple.screensaver"

def prefs(app_id, user_dom, host_dom):
	domain_keys = CFPreferencesCopyKeyList(app_id, user_dom, host_dom)
	domain_dict = CFPreferencesCopyMultiple(domain_keys, app_id, user_dom, host_dom)
	return domain_dict
	
print "~/Library/Preferences/ByHost/" + app_id
print prefs(app_id, kCFPreferencesCurrentUser, kCFPreferencesCurrentHost)
print
print "~/Library/Preferences/" + app_id
print prefs(app_id, kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
print
print "/Library/Preferences/" + app_id
print prefs(app_id, kCFPreferencesAnyUser, kCFPreferencesCurrentHost)
