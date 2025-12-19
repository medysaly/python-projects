import re

log = "System update started. Error code: 404. Contact support."
pattern = r"Error"

result = re.search(pattern, log)
if result:
    print(f"Match found: {result.group()}") # Output: Error
    print(f"Starts at index: {result.start()}") # Output: 23