tell application "CotEditor"
	try
		set theFile to path of front document
		tell application "Finder"
			reveal theFile
			activate
		end tell
	on error
		display dialog "Please save the document first before revealing in Finder." buttons {"OK"} default button "OK"
	end try
end tell
