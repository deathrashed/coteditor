tell application "CotEditor"
	try
		set theFile to path of front document
		tell application "Obsidian"
			open theFile
			activate
		end tell
	on error
		display dialog "Please save the document first before opening with Obsidian." buttons {"OK"} default button "OK"
	end try
end tell
