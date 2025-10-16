#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
CSS to SCSS Converter - Python Script for CotEditor

Convert CSS code to SCSS with basic nesting and variables.
"""

import sys
import re


def css_to_scss(css_code):
    """Convert CSS code to SCSS."""
    scss_code = css_code
    
    # Add basic nesting for related selectors
    scss_code = add_nesting(scss_code)
    
    # Convert color values to variables
    scss_code = extract_color_variables(scss_code)
    
    # Add basic mixins for repeated patterns
    scss_code = extract_mixins(scss_code)
    
    return scss_code


def add_nesting(css):
    """Add basic nesting to related selectors."""
    # This is a simplified nesting implementation
    # Look for selectors that might be related (e.g., .container .item)
    lines = css.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        if line and not line.startswith('/*'):
            # Check if this selector contains another selector
            if ' ' in line and not line.startswith('@'):
                # Split the selector
                parts = line.split(' ')
                if len(parts) == 2:
                    parent, child = parts
                    # Look for the child selector in following lines
                    result.append(f"{parent} {{")
                    # Add the child selector with proper indentation
                    child_selector = child.replace('.', '&.')
                    result.append(f"  {child_selector}")
                    # Skip the next few lines if they contain the child selector
                    i += 1
                    while i < len(lines) and lines[i].strip().startswith('}'):
                        i += 1
                    result.append("}")
                else:
                    result.append(line)
            else:
                result.append(line)
        else:
            result.append(line)
        
        i += 1
    
    return '\n'.join(result)


def extract_color_variables(css):
    """Extract color values and convert to SCSS variables."""
    # Find color values
    color_pattern = r'#[0-9a-fA-F]{3,6}'
    colors = re.findall(color_pattern, css)
    
    if colors:
        # Create variables section
        variables = []
        variable_map = {}
        
        for i, color in enumerate(colors):
            if color not in variable_map:
                var_name = f"$color-{i+1}"
                variable_map[color] = var_name
                variables.append(f"{var_name}: {color};")
        
        # Replace colors with variables
        for color, var_name in variable_map.items():
            css = css.replace(color, var_name)
        
        # Add variables at the top
        if variables:
            css = "// Color Variables\n" + '\n'.join(variables) + "\n\n" + css
    
    return css


def extract_mixins(css):
    """Extract common patterns as mixins."""
    # Look for repeated patterns (simplified)
    # This would be more complex in a real implementation
    
    # Look for common flexbox patterns
    flex_pattern = r'display:\s*flex;'
    if re.search(flex_pattern, css):
        mixin = """
@mixin flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

@mixin flex-between {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
"""
        css = mixin + css
    
    return css


def main():
    in_text = sys.stdin.read()
    if in_text:
        result = css_to_scss(in_text)
        sys.stdout.write(result)
    else:
        sys.stdout.write("No CSS code selected for conversion.")


if __name__ == "__main__":
    main()
