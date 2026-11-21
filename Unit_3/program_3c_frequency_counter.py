from pathlib import Path


log_file = Path(__file__).with_name("app.log")

# Create a sample log file
with log_file.open("w", encoding="utf-8") as file:
    file.write("INFO: Application started\n")
    file.write("WARNING: Low memory\n")
    file.write("ERROR: File not found\n")

print("LOG FILE CONTENT")
with log_file.open("r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
