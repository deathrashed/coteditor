#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Generate a random password (default 16 characters)

LENGTH=16

# Generate random password using alphanumeric characters and common symbols
openssl rand -base64 32 | tr -d "=+/" | cut -c1-$LENGTH
