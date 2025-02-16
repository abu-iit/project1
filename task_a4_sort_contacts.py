import json

# Load contacts
with open('contacts.json', 'r') as f:
    contacts = json.load(f)

# Sort by last_name, then first_name
contacts.sort(key=lambda x: (x['last_name'], x['first_name']))

# Save sorted contacts
with open('data/contacts-sorted.json', 'w') as f:
    json.dump(contacts, f, indent=4)

print("Contacts sorted and saved to data/contacts-sorted.json")
