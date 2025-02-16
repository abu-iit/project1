import os
import json
from pathlib import Path

docs_dir = Path('docs')
output_file = 'docs/index.json'

index = {}

# Find all .md files (recursively)
for md_file in docs_dir.rglob('*.md'):
    relative_path = md_file.relative_to(docs_dir)

    # Extract the first H1 title
    title = None
    with open(md_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('# '):  # H1 found
                title = line[2:].strip()
                break

    if title:
        index[str(relative_path)] = title

# Write to JSON file
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(index, f, indent=4, ensure_ascii=False)

print(f"Index created with {len(index)} entries: {output_file}")
