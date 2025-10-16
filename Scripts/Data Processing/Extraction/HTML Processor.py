#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
HTML Processor - Python Script for CotEditor

Process HTML content with various operations.
"""

import sys
import re
from html import escape, unescape


def process_html(text, operation="clean"):
    """Process HTML based on the specified operation."""
    if operation == "clean":
        return clean_html(text)
    elif operation == "escape":
        return escape_html(text)
    elif operation == "unescape":
        return unescape_html(text)
    elif operation == "extract_text":
        return extract_text_from_html(text)
    elif operation == "extract_links":
        return extract_links_from_html(text)
    elif operation == "format":
        return format_html(text)
    else:
        return text


def clean_html(text):
    """Remove HTML tags and clean the text."""
    # Remove HTML tags
    clean = re.sub(r'<[^>]+>', '', text)
    # Decode HTML entities
    clean = unescape(clean)
    # Clean up whitespace
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean


def escape_html(text):
    """Escape HTML special characters."""
    return escape(text)


def unescape_html(text):
    """Unescape HTML entities."""
    return unescape(text)


def extract_text_from_html(text):
    """Extract plain text from HTML."""
    # Remove script and style elements
    text = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', text, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Decode HTML entities
    text = unescape(text)
    
    # Clean up whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


def extract_links_from_html(text):
    """Extract links from HTML."""
    links = []
    
    # Find all anchor tags
    anchor_pattern = r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>'
    matches = re.findall(anchor_pattern, text, re.DOTALL | re.IGNORECASE)
    
    for href, link_text in matches:
        link_text = re.sub(r'<[^>]+>', '', link_text).strip()
        links.append(f"{href} - {link_text}")
    
    return '\n'.join(links) if links else "No links found"


def format_html(text):
    """Basic HTML formatting (indentation)."""
    # This is a simplified formatter
    formatted = text
    
    # Add line breaks before and after block elements
    block_elements = ['html', 'head', 'body', 'div', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    
    for element in block_elements:
        # Opening tags
        formatted = re.sub(f'<{element}[^>]*>', f'\n<{element}>', formatted, flags=re.IGNORECASE)
        # Closing tags
        formatted = re.sub(f'</{element}>', f'</{element}>\n', formatted, flags=re.IGNORECASE)
    
    # Clean up extra whitespace
    formatted = re.sub(r'\n\s*\n', '\n', formatted)
    
    return formatted.strip()


def main():
    in_text = sys.stdin.read()
    if in_text:
        # For this example, we'll clean HTML
        # In a real implementation, you might add a dialog to choose operation
        result = process_html(in_text, "clean")
        sys.stdout.write(result)
    else:
        sys.stdout.write("No HTML content selected.")


if __name__ == "__main__":
    main()
