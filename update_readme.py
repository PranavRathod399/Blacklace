import os
import glob

log_folder = "docs/Daily_logs"
readme_path = "README.md"
marker = "<!-- RECENT_JOURNAL -->"

# Find the most recent markdown file by date in the filename
log_files = sorted(glob.glob(f"{log_folder}/*.md"), reverse=True)
latest_log = log_files[0] if log_files else None

if not latest_log:
    print("No journal file found.")
    exit()

with open(latest_log, "r", encoding="utf-8") as f:
    latest_content = f.read()

with open(readme_path, "r", encoding="utf-8") as f:
    readme = f.read()

if marker in readme:
    before = readme.split(marker)[0] + marker
    updated = before + "\n\n" + latest_content
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"README updated with {latest_log}")
else:
    print("Marker not found in README.")
