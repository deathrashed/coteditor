#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
JSON Schema Generator - Python Script for CotEditor

Generate JSON Schema from JSON data.
"""

import sys
import json
from collections import defaultdict


def generate_schema(data):
    """Generate JSON Schema from data."""
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": get_type(data),
        "properties": {},
        "required": []
    }
    
    if isinstance(data, dict):
        for key, value in data.items():
            schema["properties"][key] = generate_schema(value)
            schema["required"].append(key)
    elif isinstance(data, list) and data:
        # Use first item to determine array item schema
        schema["items"] = generate_schema(data[0])
    
    return schema


def get_type(data):
    """Determine the JSON type of data."""
    if isinstance(data, bool):
        return "boolean"
    elif isinstance(data, int):
        return "integer"
    elif isinstance(data, float):
        return "number"
    elif isinstance(data, str):
        return "string"
    elif isinstance(data, list):
        return "array"
    elif isinstance(data, dict):
        return "object"
    elif data is None:
        return "null"
    else:
        return "string"


def analyze_json_structure(data, path="root"):
    """Analyze JSON structure and return detailed information."""
    analysis = {
        "type": get_type(data),
        "path": path,
        "description": ""
    }
    
    if isinstance(data, dict):
        analysis["properties"] = {}
        analysis["required"] = list(data.keys())
        
        for key, value in data.items():
            analysis["properties"][key] = analyze_json_structure(value, f"{path}.{key}")
    
    elif isinstance(data, list):
        analysis["items"] = []
        analysis["count"] = len(data)
        
        if data:
            # Analyze first few items
            for i, item in enumerate(data[:3]):
                analysis["items"].append(analyze_json_structure(item, f"{path}[{i}]"))
    
    return analysis


def format_schema(schema):
    """Format schema with proper indentation."""
    return json.dumps(schema, indent=2, sort_keys=True)


def main():
    in_text = sys.stdin.read()
    if in_text:
        try:
            data = json.loads(in_text)
            
            # Generate schema
            schema = generate_schema(data)
            formatted_schema = format_schema(schema)
            
            sys.stdout.write(formatted_schema)
            
        except json.JSONDecodeError as e:
            sys.stdout.write(f"JSON Error: {e}")
        except Exception as e:
            sys.stdout.write(f"Error: {e}")
    else:
        sys.stdout.write("No JSON data selected.")


if __name__ == "__main__":
    main()
