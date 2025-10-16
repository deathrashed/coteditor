#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
Data Validator - Python Script for CotEditor

Validate various data formats and structures.
"""

import sys
import json
import csv
import re
import email
from datetime import datetime


def validate_data(text, data_type="auto"):
    """Validate data based on the specified type."""
    if data_type == "auto":
        data_type = detect_data_type(text)
    
    if data_type == "json":
        return validate_json(text)
    elif data_type == "csv":
        return validate_csv(text)
    elif data_type == "email":
        return validate_emails(text)
    elif data_type == "phone":
        return validate_phones(text)
    elif data_type == "url":
        return validate_urls(text)
    elif data_type == "date":
        return validate_dates(text)
    else:
        return "Unknown data type"


def detect_data_type(text):
    """Auto-detect the data type."""
    text = text.strip()
    
    # Check for JSON
    if text.startswith('{') or text.startswith('['):
        try:
            json.loads(text)
            return "json"
        except:
            pass
    
    # Check for CSV
    if ',' in text and '\n' in text:
        try:
            csv.Sniffer().sniff(text[:1024])
            return "csv"
        except:
            pass
    
    # Check for emails
    if '@' in text and re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text):
        return "email"
    
    # Check for URLs
    if re.search(r'https?://', text):
        return "url"
    
    # Check for phone numbers
    if re.search(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', text):
        return "phone"
    
    return "unknown"


def validate_json(text):
    """Validate JSON data."""
    try:
        data = json.loads(text)
        return f"✓ Valid JSON\nType: {type(data).__name__}\nSize: {len(str(data))} characters"
    except json.JSONDecodeError as e:
        return f"✗ Invalid JSON\nError: {e}"


def validate_csv(text):
    """Validate CSV data."""
    try:
        csv.Sniffer().sniff(text[:1024])
        reader = csv.reader(text.splitlines())
        rows = list(reader)
        
        if not rows:
            return "✗ Empty CSV data"
        
        num_cols = len(rows[0])
        num_rows = len(rows)
        
        # Check for consistent column count
        inconsistent_rows = [i for i, row in enumerate(rows) if len(row) != num_cols]
        
        result = f"✓ Valid CSV\nRows: {num_rows}\nColumns: {num_cols}"
        
        if inconsistent_rows:
            result += f"\n⚠ Warning: Inconsistent column count in rows: {inconsistent_rows}"
        
        return result
        
    except csv.Error as e:
        return f"✗ Invalid CSV\nError: {e}"


def validate_emails(text):
    """Validate email addresses."""
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    
    results = []
    valid_count = 0
    
    for email_addr in emails:
        try:
            email.utils.parseaddr(email_addr)
            if email.utils.parseaddr(email_addr)[1]:
                results.append(f"✓ {email_addr}")
                valid_count += 1
            else:
                results.append(f"✗ {email_addr} (Invalid format)")
        except Exception:
            results.append(f"✗ {email_addr} (Invalid format)")
    
    summary = f"Email Validation Results:\nValid: {valid_count}/{len(emails)}"
    return summary + "\n" + "\n".join(results) if results else "No email addresses found"


def validate_phones(text):
    """Validate phone numbers."""
    phone_patterns = [
        r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',  # US format
        r'\b\(\d{3}\)\s?\d{3}[-.]?\d{4}\b',  # US with parentheses
        r'\b\+1[-.]?\d{3}[-.]?\d{3}[-.]?\d{4}\b',  # US with country code
    ]
    
    phones = []
    for pattern in phone_patterns:
        phones.extend(re.findall(pattern, text))
    
    results = []
    for phone in phones:
        # Clean the phone number
        clean_phone = re.sub(r'[^\d]', '', phone)
        if len(clean_phone) == 10:
            results.append(f"✓ {phone}")
        elif len(clean_phone) == 11 and clean_phone.startswith('1'):
            results.append(f"✓ {phone}")
        else:
            results.append(f"✗ {phone} (Invalid length)")
    
    return "Phone Validation Results:\n" + "\n".join(results) if results else "No phone numbers found"


def validate_urls(text):
    """Validate URLs."""
    url_pattern = r'https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:[\w.])*)?)?'
    urls = re.findall(url_pattern, text)
    
    results = []
    for url in urls:
        # Basic URL validation
        if re.match(r'^https?://', url) and '.' in url:
            results.append(f"✓ {url}")
        else:
            results.append(f"✗ {url}")
    
    return "URL Validation Results:\n" + "\n".join(results) if results else "No URLs found"


def validate_dates(text):
    """Validate date formats."""
    date_patterns = [
        r'\b\d{4}-\d{2}-\d{2}\b',  # YYYY-MM-DD
        r'\b\d{2}/\d{2}/\d{4}\b',  # MM/DD/YYYY
        r'\b\d{2}-\d{2}-\d{4}\b',  # MM-DD-YYYY
        r'\b\d{1,2}/\d{1,2}/\d{4}\b',  # M/D/YYYY
    ]
    
    dates = []
    for pattern in date_patterns:
        dates.extend(re.findall(pattern, text))
    
    results = []
    for date_str in dates:
        try:
            # Try different date formats
            for fmt in ['%Y-%m-%d', '%m/%d/%Y', '%d-%m-%Y']:
                try:
                    datetime.strptime(date_str, fmt)
                    results.append(f"✓ {date_str} ({fmt})")
                    break
                except ValueError:
                    continue
            else:
                results.append(f"✗ {date_str} (Invalid format)")
        except Exception:
            results.append(f"✗ {date_str} (Invalid date)")
    
    return "Date Validation Results:\n" + "\n".join(results) if results else "No dates found"


def main():
    in_text = sys.stdin.read()
    if in_text:
        result = validate_data(in_text)
        sys.stdout.write(result)
    else:
        sys.stdout.write("No data selected for validation.")


if __name__ == "__main__":
    main()
