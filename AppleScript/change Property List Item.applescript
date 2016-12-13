tell application "System Events"
	set sample_file to file "sample.plist" of container of (path to me)
	set sample_plist to property list file (path of sample_file)
	set negativeItem to property list item "negative" of property list item "special numbers" of sample_plist
	set value of negativeItem to (value of negativeItem) - 1
end tell