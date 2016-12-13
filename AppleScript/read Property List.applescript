tell application "System Events"
	set sample_file to file "sample.plist" of container of (path to me)
	set sample_plist to property list file (path of sample_file)
	get kind of property list item "colors" of sample_plist
	set theColors to value of property list item "colors" of sample_plist
	get count of theColors
	get last item of theColors
	
	-- alternative
	--get value of last property list item of property list item "colors" of sample_plist
end tell