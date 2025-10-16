#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
JSON to YAML Converter - Python Script for CotEditor

Convert JSON data to YAML format.
"""

import sys
import json
import yaml


def json_to_yaml(json_text):
    """Convert JSON text to YAML format."""
    try:
        # Parse JSON
        data = json.loads(json_text)
        
        # Convert to YAML
        yaml_output = yaml.dump(data, default_flow_style=False, sort_keys=False, indent=2)
        
        return yaml_output
        
    except json.JSONDecodeError as e:
        return f"JSON Error: {e}"
    except yaml.YAMLError as e:
        return f"YAML Error: {e}"
    except Exception as e:
        return f"Error: {e}"


def main():
    in_text = sys.stdin.read()
    if in_text:
        result = json_to_yaml(in_text)
        sys.stdout.write(result)
    else:
        sys.stdout.write("No JSON data selected for conversion.")


if __name__ == "__main__":
    main()
