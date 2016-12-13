tell application "System Events"
	set sample_file to file "sample.plist" of container of (path to me)
	set sample_plist to property list file (path of sample_file)
	set theDates to property list item "calendar dates for 2017" of sample_plist
	make new property list item at end of theDates with properties {kind:date, name:"TIL about Property Lists", value:current date}
end tell