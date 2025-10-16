#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
Markdown to HTML Converter - Python Script for CotEditor

Convert Markdown text to HTML format.
"""

import sys
import re


def markdown_to_html(markdown_text):
    """Convert Markdown text to HTML format."""
    html = markdown_text
    
    # Headers
    html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    
    # Bold and italic
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    
    # Code
    html = re.sub(r'`(.*?)`', r'<code>\1</code>', html)
    
    # Links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)
    
    # Images
    html = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', html)
    
    # Line breaks
    html = re.sub(r'\n\n', '</p><p>', html)
    html = re.sub(r'\n', '<br>', html)
    
    # Wrap in paragraph tags
    html = f'<p>{html}</p>'
    
    # Clean up empty paragraphs
    html = re.sub(r'<p></p>', '', html)
    html = re.sub(r'<p><br></p>', '<br>', html)
    
    return html


def main():
    in_text = sys.stdin.read()
    if in_text:
        result = markdown_to_html(in_text)
        sys.stdout.write(result)
    else:
        sys.stdout.write("No Markdown text selected for conversion.")


if __name__ == "__main__":
    main()
