#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
JavaScript to TypeScript Converter - Python Script for CotEditor

Convert JavaScript code to TypeScript with basic type annotations.
"""

import sys
import re


def js_to_ts(javascript_code):
    """Convert JavaScript code to TypeScript."""
    ts_code = javascript_code
    
    # Add basic type annotations for function parameters
    ts_code = add_function_types(ts_code)
    
    # Add type annotations for variables
    ts_code = add_variable_types(ts_code)
    
    # Add interface definitions for objects
    ts_code = add_object_types(ts_code)
    
    return ts_code


def add_function_types(code):
    """Add type annotations to function parameters."""
    # Function declaration with parameters
    pattern = r'function\s+(\w+)\s*\(([^)]*)\)'
    
    def replace_function(match):
        func_name = match.group(1)
        params = match.group(2)
        
        if params.strip():
            # Add basic types to parameters
            typed_params = []
            for param in params.split(','):
                param = param.strip()
                if param:
                    # Simple type inference based on parameter name
                    if param.startswith('str') or param.startswith('text') or param.startswith('msg'):
                        typed_params.append(f"{param}: string")
                    elif param.startswith('num') or param.startswith('count') or param.startswith('id'):
                        typed_params.append(f"{param}: number")
                    elif param.startswith('bool') or param.startswith('is') or param.startswith('has'):
                        typed_params.append(f"{param}: boolean")
                    elif param.startswith('arr') or param.startswith('list') or param.endswith('s'):
                        typed_params.append(f"{param}: any[]")
                    elif param.startswith('obj') or param.startswith('data'):
                        typed_params.append(f"{param}: any")
                    else:
                        typed_params.append(f"{param}: any")
            
            return f"function {func_name}({', '.join(typed_params)})"
        else:
            return f"function {func_name}()"
    
    return re.sub(pattern, replace_function, code)


def add_variable_types(code):
    """Add type annotations to variable declarations."""
    # const/let/var declarations
    patterns = [
        (r'const\s+(\w+)\s*=\s*([^;]+);', r'const \1: any = \2;'),
        (r'let\s+(\w+)\s*=\s*([^;]+);', r'let \1: any = \2;'),
        (r'var\s+(\w+)\s*=\s*([^;]+);', r'var \1: any = \2;'),
    ]
    
    for pattern, replacement in patterns:
        code = re.sub(pattern, replacement, code)
    
    return code


def add_object_types(code):
    """Add basic object type definitions."""
    # This is a simplified version - real implementation would be more complex
    return code


def main():
    in_text = sys.stdin.read()
    if in_text:
        result = js_to_ts(in_text)
        sys.stdout.write(result)
    else:
        sys.stdout.write("No JavaScript code selected for conversion.")


if __name__ == "__main__":
    main()
