#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
HTML to Markdown Converter - Python Script for CotEditor

Convert HTML text to Markdown format.
"""

import sys
import re


def html_to_markdown(html_text):
    """Convert HTML text to Markdown format."""
    markdown = html_text
    
    # Headers
    markdown = re.sub(r'<h1>(.*?)</h1>', r'# \1', markdown, flags=re.IGNORECASE | re.DOTALL)
    markdown = re.sub(r'<h2>(.*?)</h2>', r'## \1', markdown, flags=re.IGNORECASE | re.DOTALL)
    markdown = re.sub(r'<h3>(.*?)</h3>', r'### \1', markdown, flags=re.IGNORECASE | re.DOTALL)
    markdown = re.sub(r'<h4>(.*?)</h4>', r'#### \1', markdown, flags=re.IGNORECASE | re.DOTALL)
    markdown = re.sub(r'<h5>(.*?)</h5>', r'##### \1', markdown, flags=re.IGNORECASE | re.DOTALL)
    markdown = re.sub(r'<h6>(.*?)</h6>', r'###### \1', markdown, flags=re.IGNORECASE | re.DOTALL)
    
    # Bold and italic
    markdown = re.sub(r'<strong>(.*?)</strong>', r'**\1**', markdown, flags=re.IGNORECASE | re.DOTALL)
    markdown = re.sub(r'<b>(.*?)</b>', r'**\1**', markdown, flags=re.IGNORECASE | re.DOTALL)
    markdown = re.sub(r'<em>(.*?)</em>', r'*\1*', markdown, flags=re.IGNORECASE | re.DOTALL)
    markdown = re.sub(r'<i>(.*?)</i>', r'*\1*', markdown, flags=re.IGNORECASE | re.DOTALL)
    
    # Code
    markdown = re.sub(r'<code>(.*?)</code>', r'`\1`', markdown, flags=re.IGNORECASE | re.DOTALL)
    
    # Links
    markdown = re.sub(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', markdown, flags=re.IGNORECASE | re.DOTALL)
    
    # Images
    markdown = re.sub(r'<img[^>]*src=["\']([^"\']*)["\'][^>]*alt=["\']([^"\']*)["\'][^>]*>', r'![\2](\1)', markdown, flags=re.IGNORECASE)
    markdown = re.sub(r'<img[^>]*alt=["\']([^"\']*)["\'][^>]*src=["\']([^"\']*)["\'][^>]*>', r'![\1](\2)', markdown, flags=re.IGNORECASE)
    
    # Line breaks
    markdown = re.sub(r'<br[^>]*>', '\n', markdown, flags=re.IGNORECASE)
    markdown = re.sub(r'</p>\s*<p>', '\n\n', markdown, flags=re.IGNORECASE)
    
    # Remove remaining HTML tags
    markdown = re.sub(r'<[^>]+>', '', markdown)
    
    # Clean up whitespace
    markdown = re.sub(r'\n\s*\n', '\n\n', markdown)
    markdown = markdown.strip()
    
    return markdown


def main():
    in_text = sys.stdin.read()
    if in_text:
        result = html_to_markdown(in_text)
        sys.stdout.write(result)
    else:
        sys.stdout.write("No HTML text selected for conversion.")


if __name__ == "__main__":
    main()
