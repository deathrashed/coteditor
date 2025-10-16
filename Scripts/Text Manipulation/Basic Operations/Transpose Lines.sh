#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Transpose text (swap rows and columns)
# Useful for converting vertical lists to horizontal

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to transpose"
    exit 0
fi

awk '{for(i=1;i<=NF;i++) a[i,NR]=$i; max=(max<NF?NF:max)} END {for(i=1;i<=max;i++) {for(j=1;j<=NR;j++) printf "%s%s", a[i,j], (j==NR?"\n":"\t")}}'
