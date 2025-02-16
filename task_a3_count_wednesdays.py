from datetime import datetime

# Read dates from file
with open('dates.txt', 'r') as f:
    dates = f.readlines()

# Possible date formats (add more if needed)
date_formats = [
    "%d-%b-%Y",      # 24-Jul-2017
    "%b %d, %Y",     # Jun 16, 2004
    "%Y-%m-%d",      # 2017-07-24
    "%Y/%m/%d %H:%M:%S",  # 2009/04/12 22:19:41
]

def parse_date(date_str):
    for fmt in date_formats:
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            pass
    raise ValueError(f"Date format not recognized: {date_str}")

# Count Wednesdays
wednesday_count = sum(
    1 for date in dates if parse_date(date).weekday() == 2
)

# Write result to file
with open('data/dates-wednesdays.txt', 'w') as f:
    f.write(str(wednesday_count) + '\n')

print(f"Number of Wednesdays: {wednesday_count}")
