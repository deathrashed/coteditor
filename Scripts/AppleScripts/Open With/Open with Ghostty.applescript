tell application "CotEditor"
	try
		set theFile to path of front document
		tell application "Ghostty"
			do script "open " & quoted form of theFile
			activate
		end tell
	on error
		display dialog "Please save the document first before opening in Ghostty." buttons {"OK"} default button "OK"
	end try
end tell
