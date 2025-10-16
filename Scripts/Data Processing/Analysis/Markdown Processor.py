#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
Markdown Processor - Python Script for CotEditor

Process and manipulate Markdown content.
"""

import sys
import re


def process_markdown(text, operation="info"):
    """Process Markdown based on the specified operation."""
    if operation == "info":
        return get_markdown_info(text)
    elif operation == "toc":
        return generate_toc(text)
    elif operation == "clean":
        return clean_markdown(text)
    elif operation == "extract_links":
        return extract_markdown_links(text)
    elif operation == "extract_images":
        return extract_markdown_images(text)
    elif operation == "validate":
        return validate_markdown(text)
    else:
        return text


def get_markdown_info(text):
    """Get information about Markdown content."""
    info = []
    info.append("=== MARKDOWN INFORMATION ===")
    
    # Basic stats
    lines = text.split('\n')
    info.append(f"Lines: {len(lines)}")
    info.append(f"Characters: {len(text)}")
    info.append(f"Words: {len(text.split())}")
    
    # Count elements
    headers = len(re.findall(r'^#+\s+', text, re.MULTILINE))
    links = len(re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text))
    images = len(re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', text))
    code_blocks = len(re.findall(r'```', text)) // 2
    inline_code = len(re.findall(r'`[^`]+`', text))
    lists = len(re.findall(r'^\s*[-*+]\s+', text, re.MULTILINE))
    numbered_lists = len(re.findall(r'^\s*\d+\.\s+', text, re.MULTILINE))
    
    info.append(f"\nContent Elements:")
    info.append(f"  Headers: {headers}")
    info.append(f"  Links: {links}")
    info.append(f"  Images: {images}")
    info.append(f"  Code blocks: {code_blocks}")
    info.append(f"  Inline code: {inline_code}")
    info.append(f"  Bullet lists: {lists}")
    info.append(f"  Numbered lists: {numbered_lists}")
    
    # Header structure
    headers_found = re.findall(r'^(#+)\s+(.+)', text, re.MULTILINE)
    if headers_found:
        info.append(f"\nHeader Structure:")
        for level, title in headers_found:
            indent = "  " * (len(level) - 1)
            info.append(f"{indent}{level} {title}")
    
    return '\n'.join(info)


def generate_toc(text):
    """Generate table of contents from headers."""
    headers = re.findall(r'^(#+)\s+(.+)', text, re.MULTILINE)
    
    if not headers:
        return "No headers found for table of contents."
    
    toc = []
    toc.append("# Table of Contents\n")
    
    for level, title in headers:
        # Create anchor link
        anchor = re.sub(r'[^\w\s-]', '', title).strip().lower()
        anchor = re.sub(r'[-\s]+', '-', anchor)
        
        # Indent based on header level
        indent = "  " * (len(level) - 1)
        
        # Create TOC entry
        toc.append(f"{indent}- [{title}](#{anchor})")
    
    return '\n'.join(toc)


def clean_markdown(text):
    """Clean Markdown by removing extra whitespace and formatting issues."""
    # Remove trailing whitespace from lines
    lines = [line.rstrip() for line in text.split('\n')]
    
    # Remove multiple consecutive empty lines
    cleaned_lines = []
    prev_empty = False
    
    for line in lines:
        if line.strip() == "":
            if not prev_empty:
                cleaned_lines.append(line)
            prev_empty = True
        else:
            cleaned_lines.append(line)
            prev_empty = False
    
    # Ensure proper spacing around headers
    result = []
    for i, line in enumerate(cleaned_lines):
        if re.match(r'^#+\s+', line):
            # Add space before header if previous line is not empty
            if i > 0 and cleaned_lines[i-1].strip() != "":
                result.append("")
        result.append(line)
    
    return '\n'.join(result)


def extract_markdown_links(text):
    """Extract all links from Markdown."""
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text)
    
    if not links:
        return "No links found."
    
    result = []
    result.append("=== MARKDOWN LINKS ===")
    
    for i, (text, url) in enumerate(links, 1):
        result.append(f"{i}. [{text}]({url})")
    
    return '\n'.join(result)


def extract_markdown_images(text):
    """Extract all images from Markdown."""
    images = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', text)
    
    if not images:
        return "No images found."
    
    result = []
    result.append("=== MARKDOWN IMAGES ===")
    
    for i, (alt, url) in enumerate(images, 1):
        result.append(f"{i}. ![{alt}]({url})")
    
    return '\n'.join(result)


def validate_markdown(text):
    """Validate Markdown syntax."""
    issues = []
    
    # Check for unclosed code blocks
    code_block_count = text.count('```')
    if code_block_count % 2 != 0:
        issues.append("Unclosed code block (```)")
    
    # Check for malformed links
    malformed_links = re.findall(r'\[([^\]]*)\]\(([^)]*)\)', text)
    for text_part, url in malformed_links:
        if not url.strip():
            issues.append(f"Empty URL in link: [{text_part}]()")
    
    # Check for malformed images
    malformed_images = re.findall(r'!\[([^\]]*)\]\(([^)]*)\)', text)
    for alt, url in malformed_images:
        if not url.strip():
            issues.append(f"Empty URL in image: ![{alt}]()")
    
    # Check for header formatting
    malformed_headers = re.findall(r'^#+[^#\s]', text, re.MULTILINE)
    for header in malformed_headers:
        issues.append(f"Header without space: {header}")
    
    if issues:
        return "=== MARKDOWN ISSUES ===\n" + "\n".join(f"⚠ {issue}" for issue in issues)
    else:
        return "✓ No Markdown syntax issues found."


def main():
    in_text = sys.stdin.read()
    if in_text:
        # For this example, we'll show Markdown info
        # In a real implementation, you might add a dialog to choose operation
        result = process_markdown(in_text, "info")
        sys.stdout.write(result)
    else:
        sys.stdout.write("No Markdown content selected.")


if __name__ == "__main__":
    main()
