#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
JavaScript Linter - Python Script for CotEditor

Basic JavaScript code quality checks and suggestions.
"""

import sys
import re


def lint_javascript(js_code):
    """Lint JavaScript code and return issues."""
    issues = []
    
    # Check for common issues
    issues.extend(check_semicolons(js_code))
    issues.extend(check_var_usage(js_code))
    issues.extend(check_console_logs(js_code))
    issues.extend(check_undefined_vars(js_code))
    issues.extend(check_string_quotes(js_code))
    issues.extend(check_function_declarations(js_code))
    issues.extend(check_arrow_functions(js_code))
    
    return format_issues(issues)


def check_semicolons(code):
    """Check for missing semicolons."""
    issues = []
    lines = code.split('\n')
    
    for i, line in enumerate(lines, 1):
        line = line.strip()
        if (line and 
            not line.startswith('//') and 
            not line.startswith('/*') and
            not line.startswith('*') and
            not line.startswith('}') and
            not line.startswith('{') and
            not line.endswith(';') and
            not line.endswith(',') and
            not line.endswith('{') and
            not line.endswith('}') and
            'function' not in line and
            'if' not in line and
            'for' not in line and
            'while' not in line and
            'switch' not in line and
            'try' not in line and
            'catch' not in line and
            'finally' not in line):
            issues.append({
                'line': i,
                'severity': 'warning',
                'message': 'Missing semicolon',
                'code': 'missing-semicolon'
            })
    
    return issues


def check_var_usage(code):
    """Check for var usage (prefer let/const)."""
    issues = []
    lines = code.split('\n')
    
    for i, line in enumerate(lines, 1):
        if re.search(r'\bvar\s+\w+', line):
            issues.append({
                'line': i,
                'severity': 'warning',
                'message': 'Use let or const instead of var',
                'code': 'no-var'
            })
    
    return issues


def check_console_logs(code):
    """Check for console.log statements."""
    issues = []
    lines = code.split('\n')
    
    for i, line in enumerate(lines, 1):
        if 'console.log' in line and not line.strip().startswith('//'):
            issues.append({
                'line': i,
                'severity': 'info',
                'message': 'Consider removing console.log before production',
                'code': 'no-console'
            })
    
    return issues


def check_undefined_vars(code):
    """Check for potentially undefined variables."""
    issues = []
    
    # Simple check for common undefined variables
    undefined_patterns = [
        (r'\bundefined\b', 'undefined'),
        (r'\bnull\b', 'null'),
    ]
    
    lines = code.split('\n')
    for i, line in enumerate(lines, 1):
        for pattern, var_name in undefined_patterns:
            if re.search(pattern, line):
                issues.append({
                    'line': i,
                    'severity': 'info',
                    'message': f'Check usage of {var_name}',
                    'code': f'check-{var_name}'
                })
    
    return issues


def check_string_quotes(code):
    """Check for consistent string quotes."""
    issues = []
    lines = code.split('\n')
    
    for i, line in enumerate(lines, 1):
        # Check for mixed quotes
        if "'" in line and '"' in line:
            issues.append({
                'line': i,
                'severity': 'style',
                'message': 'Use consistent string quotes',
                'code': 'consistent-quotes'
            })
    
    return issues


def check_function_declarations(code):
    """Check function declarations."""
    issues = []
    lines = code.split('\n')
    
    for i, line in enumerate(lines, 1):
        # Check for function declarations without spacing
        if re.search(r'function\w', line):
            issues.append({
                'line': i,
                'severity': 'style',
                'message': 'Add space after function keyword',
                'code': 'function-spacing'
            })
    
    return issues


def check_arrow_functions(code):
    """Check arrow function usage."""
    issues = []
    lines = code.split('\n')
    
    for i, line in enumerate(lines, 1):
        # Check for function expressions that could be arrow functions
        if re.search(r'function\s*\(\s*\)\s*{', line):
            issues.append({
                'line': i,
                'severity': 'suggestion',
                'message': 'Consider using arrow function',
                'code': 'prefer-arrow'
            })
    
    return issues


def format_issues(issues):
    """Format issues into readable output."""
    if not issues:
        return "✓ No JavaScript linting issues found!"
    
    output = []
    output.append("=== JAVASCRIPT LINTING RESULTS ===\n")
    
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
        result = lint_javascript(in_text)
        sys.stdout.write(result)
    else:
        sys.stdout.write("No JavaScript code selected for linting.")


if __name__ == "__main__":
    main()
