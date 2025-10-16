#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
JSON to CSV Converter - Python Script for CotEditor

Convert JSON data to CSV format.
"""

import sys
import json
import csv
import io


def json_to_csv(json_text):
    """Convert JSON text to CSV format."""
    try:
        # Parse JSON
        data = json.loads(json_text)
        
        if not data:
            return ""
        
        output = io.StringIO()
        
        if isinstance(data, list) and data:
            # Array of objects
            if isinstance(data[0], dict):
                fieldnames = data[0].keys()
                writer = csv.DictWriter(output, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            else:
                # Array of values
                writer = csv.writer(output)
                writer.writerows(data)
        elif isinstance(data, dict):
            # Object with arrays as values
            writer = csv.writer(output)
            
            # Get all unique keys
            all_keys = set()
            for value in data.values():
                if isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict):
                            all_keys.update(item.keys())
            
            if all_keys:
                writer.writerow(list(all_keys))
                # This is a simplified conversion - may need more complex logic
                # depending on the JSON structure
            else:
                # Simple key-value pairs
                writer.writerow(['Key', 'Value'])
                for key, value in data.items():
                    writer.writerow([key, value])
        
        return output.getvalue()
        
    except json.JSONDecodeError as e:
        return f"JSON Error: {e}"
    except Exception as e:
        return f"Error: {e}"


def main():
    in_text = sys.stdin.read()
    if in_text:
        result = json_to_csv(in_text)
        sys.stdout.write(result)
    else:
        sys.stdout.write("No JSON data selected for conversion.")


if __name__ == "__main__":
    main()
