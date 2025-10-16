#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
Smart Line Numbers - Python Script for CotEditor

Add line numbers with proper padding and customizable separators.
Based on the template but enhanced with more options.
"""

import math
import sys


def digit(number):
    """Return digit of number."""
    return int(math.log10(number)) + 1 if number > 0 else 1


def add_line_number(text, separator="|", start=1, step=1):
    """Prepend line numbers to each line with smart padding.
    
    Args:
        text (str): Text to process
        separator (str): Separator between line number and content
        start (int): Starting line number
        step (int): Step size for line numbers
    """
    lines = text.splitlines(True)
    if not lines:
        return text
    
    # Calculate padding based on the last line number
    last_line_num = start + (len(lines) - 1) * step
    pad_length = digit(last_line_num)
    
    new_text = ""
    line_number = start
    
    for line in lines:
        line_num_str = str(line_number).rjust(pad_length)
        new_text += f"{line_num_str}{separator} {line}"
        line_number += step
    
    return new_text


def main():
    in_text = sys.stdin.read()
    if in_text:
        out_text = add_line_number(in_text)
        sys.stdout.write(out_text)


if __name__ == "__main__":
    main()
