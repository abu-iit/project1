import requests
import json
from task_b1_restrict_access import safe_path


def fetch_api_data(api_url, output_file):
    response = requests.get(api_url)
    response.raise_for_status()

    with open(safe_path(output_file), 'w') as f:
        json.dump(response.json(), f, indent=4)

    print(f"Data saved to {output_file}")
