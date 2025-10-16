#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
Text Statistics - Python Script for CotEditor

Generate comprehensive statistics about selected text.
"""

import sys
import re
from collections import Counter


def analyze_text(text):
    """Analyze text and return comprehensive statistics."""
    stats = {}
    
    # Basic counts
    stats['characters'] = len(text)
    stats['characters_no_spaces'] = len(text.replace(' ', '').replace('\n', '').replace('\t', ''))
    stats['lines'] = len(text.splitlines())
    stats['words'] = len(re.findall(r'\b\w+\b', text))
    stats['sentences'] = len(re.findall(r'[.!?]+', text))
    stats['paragraphs'] = len([p for p in text.split('\n\n') if p.strip()])
    
    # Character frequency
    char_freq = Counter(text.lower())
    stats['most_common_chars'] = char_freq.most_common(10)
    
    # Word frequency
    words = re.findall(r'\b\w+\b', text.lower())
    word_freq = Counter(words)
    stats['most_common_words'] = word_freq.most_common(10)
    
    # Reading time estimate (average 200 words per minute)
    stats['reading_time_minutes'] = round(stats['words'] / 200, 1)
    
    return stats


def format_stats(stats):
    """Format statistics into a readable report."""
    report = []
    report.append("=== TEXT STATISTICS ===\n")
    
    report.append("Basic Counts:")
    report.append(f"  Characters: {stats['characters']:,}")
    report.append(f"  Characters (no spaces): {stats['characters_no_spaces']:,}")
    report.append(f"  Lines: {stats['lines']:,}")
    report.append(f"  Words: {stats['words']:,}")
    report.append(f"  Sentences: {stats['sentences']:,}")
    report.append(f"  Paragraphs: {stats['paragraphs']:,}")
    report.append(f"  Reading time: {stats['reading_time_minutes']} minutes\n")
    
    report.append("Most Common Characters:")
    for char, count in stats['most_common_chars']:
        if char.isprintable():
            report.append(f"  '{char}': {count}")
    
    report.append("\nMost Common Words:")
    for word, count in stats['most_common_words']:
        report.append(f"  '{word}': {count}")
    
    return '\n'.join(report)


def main():
    in_text = sys.stdin.read()
    if in_text:
        stats = analyze_text(in_text)
        report = format_stats(stats)
        sys.stdout.write(report)
    else:
        sys.stdout.write("No text selected for analysis.")


if __name__ == "__main__":
    main()
