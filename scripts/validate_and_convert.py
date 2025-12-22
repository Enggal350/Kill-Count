import json
import csv
import sys
import os

def validate_and_convert(jsonl_path, csv_path):
    required_fields = {'title', 'year', 'count', 'tmdb_id'}
    data = []
    
    print(f"Validating {jsonl_path}...")
    
    try:
        with open(jsonl_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Error on line {line_num}: Invalid JSON. {e}")
                    sys.exit(1)
                
                # Check for required fields
                missing_fields = required_fields - set(entry.keys())
                if missing_fields:
                    print(f"Error on line {line_num}: Missing fields {missing_fields}")
                    sys.exit(1)
                
                # Check types (basic validation)
                if not isinstance(entry['title'], str):
                    print(f"Error on line {line_num}: 'title' must be a string")
                    sys.exit(1)
                if not isinstance(entry['year'], int):
                    print(f"Error on line {line_num}: 'year' must be an integer")
                    sys.exit(1)
                if not isinstance(entry['count'], int):
                    print(f"Error on line {line_num}: 'count' must be an integer")
                    sys.exit(1)
                if not isinstance(entry['tmdb_id'], int):
                     print(f"Error on line {line_num}: 'tmdb_id' must be an integer")
                     sys.exit(1)

                data.append(entry)
                
    except FileNotFoundError:
        print(f"Error: File {jsonl_path} not found.")
        sys.exit(1)

    print(f"Validation successful. Processed {len(data)} records.")
    
    print(f"Generating {csv_path}...")
    try:
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['title', 'year', 'count', 'tmdb_id'])
            writer.writeheader()
            writer.writerows(data)
    except IOError as e:
        print(f"Error writing to CSV: {e}")
        sys.exit(1)
        
    print(f"Successfully generated {csv_path}")

if __name__ == "__main__":
    # Paths relative to the root of the repo
    jsonl_file = 'killcounts.jsonl'
    csv_file = 'killcounts.csv'
    
    validate_and_convert(jsonl_file, csv_file)
