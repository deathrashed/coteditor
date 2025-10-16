#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
YAML to JSON Converter - Python Script for CotEditor

Convert YAML data to JSON format.
"""

import sys
import json
import yaml


def yaml_to_json(yaml_text):
    """Convert YAML text to JSON format."""
    try:
        # Parse YAML
        data = yaml.safe_load(yaml_text)
        
        # Convert to JSON
        json_output = json.dumps(data, indent=2, ensure_ascii=False)
        
        return json_output
        
    except yaml.YAMLError as e:
        return f"YAML Error: {e}"
    except json.JSONEncodeError as e:
        return f"JSON Error: {e}"
    except Exception as e:
        return f"Error: {e}"


def main():
    in_text = sys.stdin.read()
    if in_text:
        result = yaml_to_json(in_text)
        sys.stdout.write(result)
    else:
        sys.stdout.write("No YAML data selected for conversion.")


if __name__ == "__main__":
    main()
