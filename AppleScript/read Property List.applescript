tell application "System Events"
	set berryPlist to property list file "/Users/armin/Projects/PropertyListsForAppleAdmins/sample_files/berry.plist"
	set berry to value of berryPlist
	get |color| of berry
end tell