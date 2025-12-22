import json
import os
import sys

def sort_killcounts(file_path):
    print(f"Sorting {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        data = []
        for line_num, line in enumerate(lines, 1):
            if line.strip():
                try:
                    data.append(json.loads(line))
                except json.JSONDecodeError as e:
                    print(f"Warning: Invalid JSON on line {line_num}: {e}")
                    # We might want to skip or fail. For now, skip.
        
        # Sort by title, case-insensitive
        # Also handle potential missing title by using empty string
        data.sort(key=lambda x: x.get('title', '').lower())
        
        with open(file_path, 'w', encoding='utf-8') as f:
            for entry in data:
                # Use compact separators to remove spaces: (',', ':')
                f.write(json.dumps(entry, separators=(',', ':'), ensure_ascii=False) + '\n')
                
        print(f"Successfully sorted {len(data)} entries.")
        
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error sorting file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Path relative to script execution
    # Assuming run from project root or scripts/
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_file = os.path.join(project_root, 'killcounts.jsonl')
    
    if not os.path.exists(target_file):
        # Fallback if script is run directly in the same folder as jsonl (unlikely but safe)
        if os.path.exists('killcounts.jsonl'):
            target_file = 'killcounts.jsonl'
            
    sort_killcounts(target_file)
