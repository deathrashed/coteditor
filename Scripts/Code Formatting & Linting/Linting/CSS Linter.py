#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
CSS Linter - Python Script for CotEditor

Basic CSS code quality checks and suggestions.
"""

import sys
import re


def lint_css(css_code):
    """Lint CSS code and return issues."""
    issues = []
    
    # Check for common issues
    issues.extend(check_missing_semicolons(css_code))
    issues.extend(check_missing_braces(css_code))
    issues.extend(check_color_format(css_code))
    issues.extend(check_units(css_code))
    issues.extend(check_z_index(css_code))
    issues.extend(check_vendor_prefixes(css_code))
    issues.extend(check_specificity(css_code))
    
    return format_css_issues(issues)


def check_missing_semicolons(css):
    """Check for missing semicolons."""
    issues = []
    lines = css.split('\n')
    
    for i, line in enumerate(lines, 1):
        line = line.strip()
        if (line and 
            not line.startswith('/*') and
            not line.startswith('*') and
            not line.startswith('}') and
            not line.startswith('{') and
            ':' in line and
            not line.endswith(';') and
            not line.endswith('{') and
            not line.endswith('}')):
            issues.append({
                'line': i,
                'severity': 'error',
                'message': 'Missing semicolon',
                'code': 'missing-semicolon'
            })
    
    return issues


def check_missing_braces(css):
    """Check for missing braces."""
    issues = []
    lines = css.split('\n')
    
    brace_count = 0
    for i, line in enumerate(lines, 1):
        brace_count += line.count('{')
        brace_count -= line.count('}')
        
        if brace_count < 0:
            issues.append({
                'line': i,
                'severity': 'error',
                'message': 'Mismatched braces',
                'code': 'mismatched-braces'
            })
    
    return issues


def check_color_format(css):
    """Check color format consistency."""
    issues = []
    lines = css.split('\n')
    
    for i, line in enumerate(lines, 1):
        # Check for hex colors
        hex_colors = re.findall(r'#[0-9a-fA-F]{3,6}', line)
        for color in hex_colors:
            if len(color) == 4:  # Short hex
                issues.append({
                    'line': i,
                    'severity': 'style',
                    'message': f'Use full hex format: {color} → {color[0] + color[1]*2 + color[2]*2 + color[3]*2}',
                    'code': 'hex-format'
                })
        
        # Check for named colors that could be hex
        named_colors = ['red', 'blue', 'green', 'black', 'white', 'gray']
        for color in named_colors:
            if f': {color}' in line or f': {color};' in line:
                issues.append({
                    'line': i,
                    'severity': 'suggestion',
                    'message': f'Consider using hex equivalent for {color}',
                    'code': 'named-color'
                })
    
    return issues


def check_units(css):
    """Check for proper unit usage."""
    issues = []
    lines = css.split('\n')
    
    for i, line in enumerate(lines, 1):
        # Check for missing units on numeric values
        if re.search(r':\s*[0-9]+\s*;', line) and not re.search(r':\s*[0-9]+\s*(px|em|rem|%|vh|vw|pt|pc|in|cm|mm|ex|ch)\s*;', line):
            issues.append({
                'line': i,
                'severity': 'warning',
                'message': 'Consider adding unit to numeric value',
                'code': 'missing-unit'
            })
        
        # Check for zero with units
        if re.search(r':\s*0\s*(px|em|rem|pt|pc|in|cm|mm|ex|ch)\s*;', line):
            issues.append({
                'line': i,
                'severity': 'style',
                'message': 'Zero values don\'t need units',
                'code': 'zero-unit'
            })
    
    return issues


def check_z_index(css):
    """Check z-index values."""
    issues = []
    lines = css.split('\n')
    
    for i, line in enumerate(lines, 1):
        if 'z-index' in line:
            match = re.search(r'z-index:\s*(-?\d+)', line)
            if match:
                value = int(match.group(1))
                if value > 1000:
                    issues.append({
                        'line': i,
                        'severity': 'warning',
                        'message': f'High z-index value ({value}) - consider using CSS custom properties',
                        'code': 'high-z-index'
                    })
    
    return issues


def check_vendor_prefixes(css):
    """Check for vendor prefixes."""
    issues = []
    lines = css.split('\n')
    
    vendor_properties = ['-webkit-', '-moz-', '-ms-', '-o-']
    
    for i, line in enumerate(lines, 1):
        for prefix in vendor_properties:
            if prefix in line:
                issues.append({
                    'line': i,
                    'severity': 'info',
                    'message': f'Vendor prefix {prefix} - check browser support',
                    'code': 'vendor-prefix'
                })
    
    return issues


def check_specificity(css):
    """Check for high specificity selectors."""
    issues = []
    lines = css.split('\n')
    
    for i, line in enumerate(lines, 1):
        line = line.strip()
        if line and not line.startswith('/*') and not line.startswith('*'):
            # Count selectors and IDs
            selector_count = line.count(',') + 1
            id_count = line.count('#')
            
            if id_count > 1:
                issues.append({
                    'line': i,
                    'severity': 'warning',
                    'message': 'High specificity selector - consider reducing ID usage',
                    'code': 'high-specificity'
                })
    
    return issues


def format_css_issues(issues):
    """Format CSS issues into readable output."""
    if not issues:
        return "✓ No CSS linting issues found!"
    
    output = []
    output.append("=== CSS LINTING RESULTS ===\n")
    
    # Group by severity
    by_severity = {}
    for issue in issues:
        severity = issue['severity']
        if severity not in by_severity:
            by_severity[severity] = []
        by_severity[severity].append(issue)
    
    # Display by severity
    severity_order = ['error', 'warning', 'info', 'style', 'suggestion']
    severity_icons = {
        'error': '❌',
        'warning': '⚠️',
        'info': 'ℹ️',
        'style': '💅',
        'suggestion': '💡'
    }
    
    for severity in severity_order:
        if severity in by_severity:
            icon = severity_icons.get(severity, '•')
            output.append(f"{icon} {severity.upper()} ({len(by_severity[severity])})")
            
            for issue in by_severity[severity]:
                output.append(f"  Line {issue['line']}: {issue['message']}")
            
            output.append("")
    
    return '\n'.join(output)


def main():
    in_text = sys.stdin.read()
    if in_text:
        result = lint_css(in_text)
        sys.stdout.write(result)
    else:
        sys.stdout.write("No CSS code selected for linting.")


if __name__ == "__main__":
    main()
