tell application "CotEditor"
	try
		set theFile to path of front document
		tell application "TextEdit"
			open theFile
			activate
		end tell
	on error
		display dialog "Please save the document first before opening with TextEdit." buttons {"OK"} default button "OK"
	end try
end tell
