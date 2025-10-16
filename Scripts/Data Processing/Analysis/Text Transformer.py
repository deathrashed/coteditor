#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
Text Transformer - Python Script for CotEditor

Advanced text transformation with multiple options.
"""

import sys
import re
import unicodedata


def transform_text(text, operation):
    """Transform text based on the specified operation."""
    if operation == "camelCase":
        return to_camel_case(text)
    elif operation == "snake_case":
        return to_snake_case(text)
    elif operation == "kebab-case":
        return to_kebab_case(text)
    elif operation == "PascalCase":
        return to_pascal_case(text)
    elif operation == "CONSTANT_CASE":
        return to_constant_case(text)
    elif operation == "sentence case":
        return to_sentence_case(text)
    elif operation == "Title Case":
        return to_title_case(text)
    elif operation == "remove_accents":
        return remove_accents(text)
    elif operation == "slug":
        return to_slug(text)
    else:
        return text


def to_camel_case(text):
    """Convert text to camelCase."""
    words = re.findall(r'\w+', text)
    if not words:
        return text
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])


def to_snake_case(text):
    """Convert text to snake_case."""
    # Insert underscore before uppercase letters
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    # Insert underscore before uppercase letters that follow lowercase
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def to_kebab_case(text):
    """Convert text to kebab-case."""
    return to_snake_case(text).replace('_', '-')


def to_pascal_case(text):
    """Convert text to PascalCase."""
    words = re.findall(r'\w+', text)
    return ''.join(word.capitalize() for word in words)


def to_constant_case(text):
    """Convert text to CONSTANT_CASE."""
    return to_snake_case(text).upper()


def to_sentence_case(text):
    """Convert text to sentence case."""
    sentences = re.split(r'([.!?]+)', text)
    result = []
    for i, part in enumerate(sentences):
        if i % 2 == 0:  # Text part
            result.append(part.strip().capitalize())
        else:  # Punctuation part
            result.append(part)
    return ' '.join(result)


def to_title_case(text):
    """Convert text to Title Case."""
    return text.title()


def remove_accents(text):
    """Remove accents from text."""
    return ''.join(c for c in unicodedata.normalize('NFD', text) 
                   if unicodedata.category(c) != 'Mn')


def to_slug(text):
    """Convert text to URL-friendly slug."""
    # Remove accents
    text = remove_accents(text)
    # Convert to lowercase
    text = text.lower()
    # Replace spaces and special chars with hyphens
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def main():
    in_text = sys.stdin.read()
    if not in_text:
        sys.stdout.write("No text selected for transformation.")
        return
    
    # For this example, we'll apply camelCase transformation
    # In a real implementation, you might want to add a dialog to choose operation
    transformed = transform_text(in_text.strip(), "camelCase")
    sys.stdout.write(transformed)


if __name__ == "__main__":
    main()
