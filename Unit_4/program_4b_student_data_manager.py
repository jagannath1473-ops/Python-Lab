import json
from pathlib import Path


log_file = Path(__file__).with_name("logs.json")
logs = [
    {"level": "INFO", "message": "Login successful"},
    {"level": "ERROR", "message": "Database unavailable"},
    {"level": "WARNING", "message": "High memory usage"},
    {"level": "ERROR", "message": "Request failed"},
]

with log_file.open("w", encoding="utf-8") as file:
    json.dump(logs, file, indent=2)

with log_file.open("r", encoding="utf-8") as file:
    data = json.load(file)

errors = [entry for entry in data if entry["level"] == "ERROR"]
print("Total logs:", len(data))
print("Errors:", len(errors))
for error in errors:
    print("-", error["message"])
