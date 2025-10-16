#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
CSV Processor - Python Script for CotEditor

Process and analyze CSV data with various operations.
"""

import sys
import csv
import io
from collections import Counter


def process_csv(text, operation="info"):
    """Process CSV data based on the specified operation."""
    try:
        csv_reader = csv.reader(io.StringIO(text))
        rows = list(csv_reader)
        
        if operation == "info":
            return get_csv_info(rows)
        elif operation == "transpose":
            return transpose_csv(rows)
        elif operation == "sort":
            return sort_csv(rows)
        elif operation == "unique":
            return remove_duplicate_rows(rows)
        elif operation == "stats":
            return csv_statistics(rows)
        else:
            return text
            
    except csv.Error as e:
        return f"CSV Error: {e}"


def get_csv_info(rows):
    """Get basic information about CSV data."""
    if not rows:
        return "No data found"
    
    info = []
    info.append("=== CSV INFORMATION ===")
    info.append(f"Rows: {len(rows)}")
    info.append(f"Columns: {len(rows[0]) if rows else 0}")
    
    if rows:
        info.append("\nColumn headers:")
        for i, header in enumerate(rows[0]):
            info.append(f"  {i+1}: {header}")
    
    # Check for empty cells
    empty_cells = 0
    total_cells = len(rows) * len(rows[0]) if rows else 0
    for row in rows:
        empty_cells += row.count('')
    
    if total_cells > 0:
        info.append(f"\nEmpty cells: {empty_cells} ({empty_cells/total_cells*100:.1f}%)")
    
    return '\n'.join(info)


def transpose_csv(rows):
    """Transpose CSV data (swap rows and columns)."""
    if not rows:
        return ""
    
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Transpose the data
    transposed = list(zip(*rows))
    
    for row in transposed:
        writer.writerow(row)
    
    return output.getvalue()


def sort_csv(rows):
    """Sort CSV data by the first column."""
    if not rows:
        return ""
    
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Keep header and sort the rest
    if len(rows) > 1:
        header = rows[0]
        data_rows = rows[1:]
        sorted_rows = sorted(data_rows, key=lambda x: x[0] if x else "")
        
        writer.writerow(header)
        for row in sorted_rows:
            writer.writerow(row)
    else:
        for row in rows:
            writer.writerow(row)
    
    return output.getvalue()


def remove_duplicate_rows(rows):
    """Remove duplicate rows from CSV data."""
    if not rows:
        return ""
    
    output = io.StringIO()
    writer = csv.writer(output)
    
    seen = set()
    for row in rows:
        row_tuple = tuple(row)
        if row_tuple not in seen:
            seen.add(row_tuple)
            writer.writerow(row)
    
    return output.getvalue()


def csv_statistics(rows):
    """Generate statistics for CSV data."""
    if not rows:
        return "No data found"
    
    stats = []
    stats.append("=== CSV STATISTICS ===")
    stats.append(f"Total rows: {len(rows)}")
    
    if len(rows) > 1:
        stats.append(f"Data rows: {len(rows) - 1}")
    
    # Column statistics
    if rows:
        num_cols = len(rows[0])
        stats.append(f"Columns: {num_cols}")
        
        for col_idx in range(num_cols):
            col_data = [row[col_idx] for row in rows[1:] if len(row) > col_idx]
            non_empty = [cell for cell in col_data if cell.strip()]
            
            stats.append(f"\nColumn {col_idx + 1} ({rows[0][col_idx] if rows else 'Unknown'}):")
            stats.append(f"  Non-empty values: {len(non_empty)}")
            
            if non_empty:
                # Try to determine if it's numeric
                try:
                    numeric_values = [float(cell) for cell in non_empty]
                    stats.append(f"  Numeric values: {len(numeric_values)}")
                    stats.append(f"  Average: {sum(numeric_values)/len(numeric_values):.2f}")
                    stats.append(f"  Min: {min(numeric_values)}")
                    stats.append(f"  Max: {max(numeric_values)}")
                except ValueError:
                    # Not numeric, show unique values
                    unique_values = set(non_empty)
                    stats.append(f"  Unique values: {len(unique_values)}")
                    if len(unique_values) <= 10:
                        stats.append(f"  Values: {', '.join(sorted(unique_values))}")
    
    return '\n'.join(stats)


def main():
    in_text = sys.stdin.read()
    if in_text:
        # For this example, we'll show CSV info
        # In a real implementation, you might add a dialog to choose operation
        result = process_csv(in_text, "info")
        sys.stdout.write(result)
    else:
        sys.stdout.write("No CSV data selected.")


if __name__ == "__main__":
    main()
