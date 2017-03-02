#!/usr/bin/python

from Foundation import CFPreferencesCopyValue, \
                       kCFPreferencesCurrentUser, \
                       kCFPreferencesAnyUser, \
                       kCFPreferencesCurrentHost, \
                       kCFPreferencesAnyHost, \
                       kCFPreferencesAnyApplication

# User's ByHost (defaults -currentHost read)
print "Screen Saver: idleTime = ",
print CFPreferencesCopyValue("idleTime", "com.apple.screensaver", kCFPreferencesCurrentUser, kCFPreferencesCurrentHost)

# User (defaults read)
print "Screen Saver: askForPassword = ",
print CFPreferencesCopyValue("askForPassword", "com.apple.screensaver", kCFPreferencesCurrentUser, kCFPreferencesAnyHost)

# User, global domain
print "Global Domain: AppleLanguages = ",
print CFPreferencesCopyValue("AppleLanguages", kCFPreferencesAnyApplication, kCFPreferencesCurrentUser, kCFPreferencesAnyHost)

# all Users (defaults read /Library/Preferences/)
print "Login Window: lastUserName = ",
print CFPreferencesCopyValue("lastUserName", "com.apple.loginwindow", kCFPreferencesAnyUser, kCFPreferencesCurrentHost)

# all Users, global
print "All Users, Global: AppleLanguages = ",
print CFPreferencesCopyValue("AppleLanguages", kCFPreferencesAnyApplication, kCFPreferencesAnyUser, kCFPreferencesCurrentHost)
