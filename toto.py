"""Print file content of README.md"""

from pathlib import Path

file_name = "README.md"
print(f"Reading content of file {file_name}")

file_content = Path(file_name).read_text()
print(f"======\n{file_content}\n======")

