tell application "CotEditor"
	try
		set theFile to path of front document
		tell application "Stickies"
			open theFile
			activate
		end tell
	on error
		display dialog "Please save the document first before opening with Stickies." buttons {"OK"} default button "OK"
	end try
end tell
