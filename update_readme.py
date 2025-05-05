log_file = "docs/Daily_logs/May-4.md"
readme_path = "README.md"
marker = "<!-- RECENT_JOURNAL -->"

# Read journal content
with open(log_file, "r", encoding="utf-8") as f:
    content = f.read()

# Update README.md
with open(readme_path, "r", encoding="utf-8") as f:
    readme = f.read()

if marker in readme:
    before = readme.split(marker)[0] + marker
    updated = before + "\n\n" + content
    with open(readme_path, "
