tell application "CotEditor"
	try
		set theFile to path of front document
		tell application "Dropover"
			open theFile
			activate
		end tell
	on error
		display dialog "Please save the document first before opening with Dropover." buttons {"OK"} default button "OK"
	end try
end tell
