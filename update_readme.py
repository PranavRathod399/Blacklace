import os

log_dir = "docs/Daily_logs"
readme_path = "README.md"
marker = "<!-- RECENT_JOURNAL -->"

# Find latest .md file
files = sorted([f for f in os.listdir(log_dir) if f.endswith(".md")])
latest = files[-1] if files else None

if latest:
    with open(os.path.join(log_dir, latest), "r", encoding="utf-8") as f:
        content = f.read()

    with open(readme_path, "r", encoding="utf-8") as f:
        readme = f.read()

    if marker in readme:
        before = readme.split(marker)[0] + marker
        updated = before + "\n\n" + content
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(updated)
