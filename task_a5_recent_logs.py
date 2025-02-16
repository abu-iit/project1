import os
from pathlib import Path

logs_dir = Path('logs')
output_file = 'logs-recent.txt'

# Get all .log files, sorted by modified time (most recent first)
log_files = sorted(
    logs_dir.glob('*.log'),
    key=lambda f: f.stat().st_mtime,
    reverse=True
)[:10]  # Take the 10 most recent

# Extract the first line of each
first_lines = []
for log_file in log_files:
    with open(log_file, 'r') as f:
        first_line = f.readline().strip()
        first_lines.append(first_line)

# Write to output file
with open(output_file, 'w') as f:
    for line in first_lines:
        f.write(line + '\n')

print(f"Extracted first lines of {len(first_lines)} recent log files to {output_file}")
