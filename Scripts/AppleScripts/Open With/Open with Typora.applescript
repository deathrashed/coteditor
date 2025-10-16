tell application "CotEditor"
	try
		set theFile to path of front document
		tell application "Typora"
			open theFile
			activate
		end tell
	on error
		display dialog "Please save the document first before opening with Typora." buttons {"OK"} default button "OK"
	end try
end tell
