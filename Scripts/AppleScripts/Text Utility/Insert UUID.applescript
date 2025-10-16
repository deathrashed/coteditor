(*
Insert UUID.applescript
Script for CotEditor

Description:
Insert a new UUID at the cursor position in the frontmost document.

written by AI Assistant
*)

--
tell application "CotEditor"
	if not (exists front document) then return
	
	set newUUID to do shell script "uuidgen"
	
	tell front document
		set selection to newUUID
	end tell
end tell
