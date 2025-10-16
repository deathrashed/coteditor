#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
Text to ASCII Art Converter - Python Script for CotEditor

Convert text to ASCII art using simple patterns.
"""

import sys


def text_to_ascii_art(text, style="block"):
    """Convert text to ASCII art."""
    if not text:
        return ""
    
    text = text.strip()
    
    if style == "block":
        return create_block_art(text)
    elif style == "bubble":
        return create_bubble_art(text)
    elif style == "frame":
        return create_frame_art(text)
    elif style == "arrow":
        return create_arrow_art(text)
    else:
        return create_block_art(text)


def create_block_art(text):
    """Create block-style ASCII art."""
    lines = []
    
    # Top border
    border = "█" * (len(text) + 4)
    lines.append(border)
    
    # Text line
    lines.append(f"█ {text} █")
    
    # Bottom border
    lines.append(border)
    
    return '\n'.join(lines)


def create_bubble_art(text):
    """Create bubble-style ASCII art."""
    lines = []
    
    # Top bubble
    top = "╭" + "─" * (len(text) + 2) + "╮"
    lines.append(top)
    
    # Text line
    lines.append(f"│ {text} │")
    
    # Bottom bubble
    bottom = "╰" + "─" * (len(text) + 2) + "╯"
    lines.append(bottom)
    
    return '\n'.join(lines)


def create_frame_art(text):
    """Create frame-style ASCII art."""
    lines = []
    
    # Top frame
    top = "┌" + "─" * (len(text) + 2) + "┐"
    lines.append(top)
    
    # Text line
    lines.append(f"│ {text} │")
    
    # Bottom frame
    bottom = "└" + "─" * (len(text) + 2) + "┘"
    lines.append(bottom)
    
    return '\n'.join(lines)


def create_arrow_art(text):
    """Create arrow-style ASCII art."""
    lines = []
    
    # Arrow pointing to text
    lines.append("    ╭─")
    lines.append(f"───→ {text}")
    lines.append("    ╰─")
    
    return '\n'.join(lines)


def main():
    in_text = sys.stdin.read()
    if in_text:
        # Default to block style
        result = text_to_ascii_art(in_text, "block")
        sys.stdout.write(result)
    else:
        sys.stdout.write("No text selected for ASCII art conversion.")


if __name__ == "__main__":
    main()
