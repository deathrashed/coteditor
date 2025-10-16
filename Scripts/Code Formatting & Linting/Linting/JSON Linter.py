#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
JSON Linter - Python Script for CotEditor

Validate and lint JSON data with detailed error reporting.
"""

import sys
import json
import re


def lint_json(json_text):
    """Lint JSON code and return issues."""
    issues = []
    
    # Basic JSON validation
    try:
        data = json.loads(json_text)
        issues.extend(check_json_structure(data, json_text))
        issues.extend(check_json_style(json_text))
        issues.extend(check_json_best_practices(data, json_text))
    except json.JSONDecodeError as e:
        issues.append({
            'line': e.lineno,
            'column': e.colno,
            'severity': 'error',
            'message': f'JSON syntax error: {e.msg}',
            'code': 'json-syntax-error'
        })
    except Exception as e:
        issues.append({
            'line': 1,
            'severity': 'error',
            'message': f'JSON error: {e}',
            'code': 'json-error'
        })
    
    return format_json_issues(issues)


def check_json_structure(data, json_text):
    """Check JSON structure and content."""
    issues = []
    
    # Check for empty objects/arrays
    if isinstance(data, dict) and not data:
        issues.append({
            'line': 1,
            'severity': 'info',
            'message': 'Empty JSON object',
            'code': 'empty-object'
        })
    elif isinstance(data, list) and not data:
        issues.append({
            'line': 1,
            'severity': 'info',
            'message': 'Empty JSON array',
            'code': 'empty-array'
        })
    
    # Check for deeply nested structures
    max_depth = get_max_depth(data)
    if max_depth > 5:
        issues.append({
            'line': 1,
            'severity': 'warning',
            'message': f'Deep nesting detected (depth: {max_depth})',
            'code': 'deep-nesting'
        })
    
    # Check for duplicate keys (this is handled by JSON parser, but we can check)
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict) and not value:
                issues.append({
                    'line': 1,
                    'severity': 'info',
                    'message': f'Empty object for key "{key}"',
                    'code': 'empty-nested-object'
                })
    
    return issues


def check_json_style(json_text):
    """Check JSON formatting and style."""
    issues = []
    lines = json_text.split('\n')
    
    for i, line in enumerate(lines, 1):
        # Check for trailing commas
        if line.strip().endswith(','):
            issues.append({
                'line': i,
                'severity': 'error',
                'message': 'Trailing comma not allowed in JSON',
                'code': 'trailing-comma'
            })
        
        # Check for single quotes
        if "'" in line and not line.strip().startswith('//'):
            issues.append({
                'line': i,
                'severity': 'error',
                'message': 'Single quotes not allowed in JSON - use double quotes',
                'code': 'single-quotes'
            })
        
        # Check for comments
        if '//' in line or '/*' in line:
            issues.append({
                'line': i,
                'severity': 'error',
                'message': 'Comments not allowed in JSON',
                'code': 'comments'
            })
        
        # Check for unquoted keys
        if re.search(r'[^"]\w+[^"]\s*:', line):
            issues.append({
                'line': i,
                'severity': 'error',
                'message': 'Object keys must be quoted in JSON',
                'code': 'unquoted-keys'
            })
    
    return issues


def check_json_best_practices(data, json_text):
    """Check JSON best practices."""
    issues = []
    
    if isinstance(data, dict):
        # Check for camelCase vs snake_case consistency
        keys = list(data.keys())
        camel_case_count = sum(1 for key in keys if re.match(r'^[a-z][a-zA-Z0-9]*$', key))
        snake_case_count = sum(1 for key in keys if re.match(r'^[a-z][a-z0-9_]*$', key))
        
        if camel_case_count > 0 and snake_case_count > 0:
            issues.append({
                'line': 1,
                'severity': 'style',
                'message': 'Mixed naming conventions - use consistent camelCase or snake_case',
                'code': 'naming-convention'
            })
        
        # Check for required fields in common structures
        if 'email' in keys and '@' not in str(data.get('email', '')):
            issues.append({
                'line': 1,
                'severity': 'warning',
                'message': 'Email field may not contain valid email format',
                'code': 'email-format'
            })
        
        # Check for date formats
        date_fields = [key for key in keys if 'date' in key.lower() or 'time' in key.lower()]
        for field in date_fields:
            value = data.get(field)
            if isinstance(value, str) and not re.match(r'^\d{4}-\d{2}-\d{2}', value):
                issues.append({
                    'line': 1,
                    'severity': 'suggestion',
                    'message': f'Consider ISO 8601 date format for "{field}"',
                    'code': 'date-format'
                })
    
    return issues


def get_max_depth(obj, depth=0):
    """Get maximum nesting depth of JSON object."""
    if isinstance(obj, dict):
        if not obj:
            return depth
        return max(get_max_depth(value, depth + 1) for value in obj.values())
    elif isinstance(obj, list):
        if not obj:
            return depth
        return max(get_max_depth(item, depth + 1) for item in obj)
    else:
        return depth


def format_json_issues(issues):
    """Format JSON issues into readable output."""
    if not issues:
        return "✓ No JSON linting issues found!"
    
    output = []
    output.append("=== JSON LINTING RESULTS ===\n")
    
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
                line_info = f"Line {issue['line']}"
                if 'column' in issue:
                    line_info += f":{issue['column']}"
                output.append(f"  {line_info}: {issue['message']}")
            
            output.append("")
    
    return '\n'.join(output)


def main():
    in_text = sys.stdin.read()
    if in_text:
        result = lint_json(in_text)
        sys.stdout.write(result)
    else:
        sys.stdout.write("No JSON data selected for linting.")


if __name__ == "__main__":
    main()
