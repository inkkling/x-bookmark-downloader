import json, os

# This must match OUTPUT_BASE in xbd3.py
OUTPUT_BASE = r'C:\Users\YourName\Pictures\X Bookmarks'
creds_file = os.path.join(OUTPUT_BASE, '_creds.json')

print("=== One-time credential setup ===")
print()
print("1. Press F12 in Chrome")
print("2. Click 'Application' tab")
print("3. Left panel: Cookies > https://x.com")
print("4. Find 'auth_token' row, copy its Value")
print()
auth_token = input("Paste your auth_token here: ").strip()

ct0 = input("Paste your ct0 cookie value here (same place, find 'ct0' row): ").strip()

creds = {"auth_token": auth_token, "ct0": ct0}
os.makedirs(os.path.dirname(creds_file), exist_ok=True)
with open(creds_file, 'w') as f:
    json.dump(creds, f)

print()
print(f"Saved to {creds_file}")
print("You only need to do this again if X logs you out.")
