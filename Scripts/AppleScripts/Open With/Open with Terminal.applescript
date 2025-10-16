tell application "CotEditor"
	try
		set theFile to path of front document
		tell application "Terminal"
			do script "open " & quoted form of theFile
			activate
		end tell
	on error
		display dialog "Please save the document first before opening in Terminal." buttons {"OK"} default button "OK"
	end try
end tell
