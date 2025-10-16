#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
CSV to JSON Converter - Python Script for CotEditor

Convert CSV data to JSON format.
"""

import sys
import csv
import json
import io


def csv_to_json(csv_text, format_type="array"):
    """Convert CSV text to JSON format.
    
    Args:
        csv_text: CSV text to convert
        format_type: 'array' for array of objects, 'object' for object with headers as keys
    """
    try:
        # Parse CSV
        csv_reader = csv.DictReader(io.StringIO(csv_text))
        data = list(csv_reader)
        
        if format_type == "array":
            # Array of objects
            json_output = json.dumps(data, indent=2, ensure_ascii=False)
        elif format_type == "object":
            # Object with headers as keys
            if data:
                headers = list(data[0].keys())
                result = {}
                for header in headers:
                    result[header] = [row[header] for row in data]
                json_output = json.dumps(result, indent=2, ensure_ascii=False)
            else:
                json_output = "{}"
        else:
            return "Invalid format type. Use 'array' or 'object'."
        
        return json_output
        
    except csv.Error as e:
        return f"CSV Error: {e}"
    except json.JSONEncodeError as e:
        return f"JSON Error: {e}"
    except Exception as e:
        return f"Error: {e}"


def main():
    in_text = sys.stdin.read()
    if in_text:
        # Default to array format
        result = csv_to_json(in_text, "array")
        sys.stdout.write(result)
    else:
        sys.stdout.write("No CSV data selected for conversion.")


if __name__ == "__main__":
    main()
