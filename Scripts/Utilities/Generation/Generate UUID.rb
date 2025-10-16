#!/usr/bin/env ruby -Ku
#%%%{CotEditorXInput=None}%%%
#%%%{CotEditorXOutput=InsertAfterSelection}%%%

# Generate a new UUID at cursor position

require 'securerandom'
print SecureRandom.uuid

exit
