#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
URL Processor - Python Script for CotEditor

Process URLs with various operations like validation, parsing, and manipulation.
"""

import sys
import urllib.parse
import re
from urllib.parse import urlparse, urljoin, urlunparse


def process_urls(text, operation="validate"):
    """Process URLs based on the specified operation."""
    urls = extract_urls(text)
    
    if operation == "validate":
        return validate_urls(urls)
    elif operation == "parse":
        return parse_urls(urls)
    elif operation == "clean":
        return clean_urls(urls)
    elif operation == "extract_domains":
        return extract_domains(urls)
    elif operation == "make_absolute":
        return make_urls_absolute(urls)
    else:
        return text


def extract_urls(text):
    """Extract all URLs from text."""
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    return re.findall(url_pattern, text)


def validate_urls(urls):
    """Validate URLs and return results."""
    results = []
    results.append("=== URL VALIDATION ===")
    
    for i, url in enumerate(urls, 1):
        try:
            parsed = urlparse(url)
            if parsed.scheme and parsed.netloc:
                results.append(f"{i}. ✓ {url}")
                results.append(f"   Scheme: {parsed.scheme}")
                results.append(f"   Domain: {parsed.netloc}")
                results.append(f"   Path: {parsed.path}")
            else:
                results.append(f"{i}. ✗ {url} (Invalid format)")
        except Exception as e:
            results.append(f"{i}. ✗ {url} (Error: {e})")
    
    return '\n'.join(results) if results else "No URLs found"


def parse_urls(urls):
    """Parse URLs and return detailed information."""
    results = []
    results.append("=== URL PARSING ===")
    
    for i, url in enumerate(urls, 1):
        try:
            parsed = urlparse(url)
            results.append(f"\n{i}. {url}")
            results.append(f"   Scheme: {parsed.scheme}")
            results.append(f"   Netloc: {parsed.netloc}")
            results.append(f"   Path: {parsed.path}")
            results.append(f"   Params: {parsed.params}")
            results.append(f"   Query: {parsed.query}")
            results.append(f"   Fragment: {parsed.fragment}")
            
            # Parse query parameters
            if parsed.query:
                query_params = urllib.parse.parse_qs(parsed.query)
                results.append(f"   Query Parameters:")
                for key, values in query_params.items():
                    results.append(f"     {key}: {', '.join(values)}")
        except Exception as e:
            results.append(f"\n{i}. {url} (Error: {e})")
    
    return '\n'.join(results) if results else "No URLs found"


def clean_urls(urls):
    """Clean URLs by removing common tracking parameters."""
    cleaned = []
    tracking_params = {'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 
                      'utm_content', 'fbclid', 'gclid', '_ga', 'ref'}
    
    for url in urls:
        try:
            parsed = urlparse(url)
            query_params = urllib.parse.parse_qs(parsed.query)
            
            # Remove tracking parameters
            cleaned_params = {k: v for k, v in query_params.items() 
                            if k not in tracking_params}
            
            # Rebuild URL
            cleaned_query = urllib.parse.urlencode(cleaned_params, doseq=True)
            cleaned_url = urlunparse((
                parsed.scheme, parsed.netloc, parsed.path,
                parsed.params, cleaned_query, parsed.fragment
            ))
            cleaned.append(cleaned_url)
        except Exception:
            cleaned.append(url)  # Keep original if cleaning fails
    
    return '\n'.join(cleaned)


def extract_domains(urls):
    """Extract domains from URLs."""
    domains = set()
    
    for url in urls:
        try:
            parsed = urlparse(url)
            if parsed.netloc:
                domains.add(parsed.netloc)
        except Exception:
            continue
    
    return '\n'.join(sorted(domains))


def make_urls_absolute(urls):
    """Convert relative URLs to absolute (requires a base URL)."""
    # For this example, we'll assume a base URL
    base_url = "https://example.com"
    
    absolute_urls = []
    for url in urls:
        try:
            if url.startswith(('http://', 'https://')):
                absolute_urls.append(url)
            else:
                absolute_url = urljoin(base_url, url)
                absolute_urls.append(absolute_url)
        except Exception:
            absolute_urls.append(url)
    
    return '\n'.join(absolute_urls)


def main():
    in_text = sys.stdin.read()
    if in_text:
        # For this example, we'll validate URLs
        # In a real implementation, you might add a dialog to choose operation
        result = process_urls(in_text, "validate")
        sys.stdout.write(result)
    else:
        sys.stdout.write("No text selected for URL processing.")


if __name__ == "__main__":
    main()
