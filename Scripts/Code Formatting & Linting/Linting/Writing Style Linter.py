#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
Writing Style Linter - Python Script for CotEditor

Analyze text for writing style, grammar, and readability issues.
"""

import sys
import re
from collections import Counter


def lint_writing(text):
    """Lint text for writing style issues."""
    issues = []
    
    # Check for common writing issues
    issues.extend(check_sentence_length(text))
    issues.extend(check_passive_voice(text))
    issues.extend(check_weasel_words(text))
    issues.extend(check_redundancy(text))
    issues.extend(check_readability(text))
    issues.extend(check_grammar_basics(text))
    issues.extend(check_word_choice(text))
    
    return format_writing_issues(issues, text)


def check_sentence_length(text):
    """Check for overly long sentences."""
    issues = []
    sentences = re.split(r'[.!?]+', text)
    
    for i, sentence in enumerate(sentences):
        sentence = sentence.strip()
        if not sentence:
            continue
        
        word_count = len(sentence.split())
        if word_count > 25:
            issues.append({
                'sentence': i + 1,
                'severity': 'warning',
                'message': f'Sentence too long ({word_count} words) - consider breaking it up',
                'code': 'long-sentence'
            })
    
    return issues


def check_passive_voice(text):
    """Check for passive voice usage."""
    issues = []
    lines = text.split('\n')
    
    passive_patterns = [
        r'\b(is|are|was|were|be|been|being)\s+\w+ed\b',
        r'\b(has|have|had)\s+been\s+\w+ed\b',
        r'\bwill\s+be\s+\w+ed\b'
    ]
    
    for i, line in enumerate(lines, 1):
        for pattern in passive_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                issues.append({
                    'line': i,
                    'severity': 'suggestion',
                    'message': 'Consider using active voice instead of passive',
                    'code': 'passive-voice'
                })
                break
    
    return issues


def check_weasel_words(text):
    """Check for weak or unclear words."""
    issues = []
    lines = text.split('\n')
    
    weasel_words = [
        'very', 'really', 'quite', 'rather', 'pretty', 'fairly',
        'somewhat', 'kind of', 'sort of', 'basically', 'essentially',
        'literally', 'actually', 'just', 'simply', 'merely'
    ]
    
    for i, line in enumerate(lines, 1):
        words = line.lower().split()
        for word in words:
            clean_word = re.sub(r'[^\w]', '', word)
            if clean_word in weasel_words:
                issues.append({
                    'line': i,
                    'severity': 'suggestion',
                    'message': f'Consider removing weak word: "{clean_word}"',
                    'code': 'weasel-word'
                })
    
    return issues


def check_redundancy(text):
    """Check for redundant phrases."""
    issues = []
    lines = text.split('\n')
    
    redundant_phrases = [
        'free gift', 'new innovation', 'past history', 'future plans',
        'end result', 'final outcome', 'basic fundamentals',
        'true facts', 'personal opinion', 'advance warning'
    ]
    
    for i, line in enumerate(lines, 1):
        line_lower = line.lower()
        for phrase in redundant_phrases:
            if phrase in line_lower:
                issues.append({
                    'line': i,
                    'severity': 'style',
                    'message': f'Redundant phrase: "{phrase}"',
                    'code': 'redundancy'
                })
    
    return issues


def check_readability(text):
    """Check text readability."""
    issues = []
    
    # Simple readability metrics
    sentences = re.split(r'[.!?]+', text)
    words = re.findall(r'\b\w+\b', text)
    
    if sentences and words:
        avg_sentence_length = len(words) / len(sentences)
        avg_word_length = sum(len(word) for word in words) / len(words)
        
        if avg_sentence_length > 20:
            issues.append({
                'line': 1,
                'severity': 'info',
                'message': f'Average sentence length is {avg_sentence_length:.1f} words (consider shorter sentences)',
                'code': 'readability-sentence'
            })
        
        if avg_word_length > 6:
            issues.append({
                'line': 1,
                'severity': 'info',
                'message': f'Average word length is {avg_word_length:.1f} characters (consider simpler words)',
                'code': 'readability-word'
            })
    
    return issues


def check_grammar_basics(text):
    """Check for basic grammar issues."""
    issues = []
    lines = text.split('\n')
    
    for i, line in enumerate(lines, 1):
        # Check for double spaces
        if '  ' in line:
            issues.append({
                'line': i,
                'severity': 'style',
                'message': 'Multiple consecutive spaces',
                'code': 'double-space'
            })
        
        # Check for missing space after punctuation
        if re.search(r'[.!?][A-Za-z]', line):
            issues.append({
                'line': i,
                'severity': 'style',
                'message': 'Missing space after punctuation',
                'code': 'missing-space'
            })
        
        # Check for common typos
        common_typos = {
            'teh': 'the',
            'adn': 'and',
            'recieve': 'receive',
            'seperate': 'separate',
            'definately': 'definitely'
        }
        
        for typo, correction in common_typos.items():
            if re.search(r'\b' + typo + r'\b', line, re.IGNORECASE):
                issues.append({
                    'line': i,
                    'severity': 'error',
                    'message': f'Possible typo: "{typo}" should be "{correction}"',
                    'code': 'typo'
                })
    
    return issues


def check_word_choice(text):
    """Check for word choice improvements."""
    issues = []
    lines = text.split('\n')
    
    word_suggestions = {
        'utilize': 'use',
        'facilitate': 'help',
        'implement': 'do',
        'leverage': 'use',
        'optimize': 'improve',
        'synergy': 'cooperation',
        'paradigm': 'model'
    }
    
    for i, line in enumerate(lines, 1):
        words = re.findall(r'\b\w+\b', line.lower())
        for word in words:
            if word in word_suggestions:
                issues.append({
                    'line': i,
                    'severity': 'suggestion',
                    'message': f'Consider simpler word: "{word}" → "{word_suggestions[word]}"',
                    'code': 'word-choice'
                })
    
    return issues


def format_writing_issues(issues, text):
    """Format writing issues into readable output."""
    if not issues:
        return "✓ No writing style issues found!"
    
    output = []
    output.append("=== WRITING STYLE ANALYSIS ===\n")
    
    # Calculate basic stats
    sentences = len(re.split(r'[.!?]+', text))
    words = len(re.findall(r'\b\w+\b', text))
    characters = len(text)
    
    output.append(f"Text Statistics:")
    output.append(f"  Sentences: {sentences}")
    output.append(f"  Words: {words}")
    output.append(f"  Characters: {characters}")
    if sentences > 0:
        output.append(f"  Average words per sentence: {words/sentences:.1f}")
    output.append("")
    
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
                if 'line' in issue:
                    output.append(f"  Line {issue['line']}: {issue['message']}")
                elif 'sentence' in issue:
                    output.append(f"  Sentence {issue['sentence']}: {issue['message']}")
            
            output.append("")
    
    return '\n'.join(output)


def main():
    in_text = sys.stdin.read()
    if in_text:
        result = lint_writing(in_text)
        sys.stdout.write(result)
    else:
        sys.stdout.write("No text selected for writing style analysis.")


if __name__ == "__main__":
    main()
