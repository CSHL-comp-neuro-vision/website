#!/usr/bin/env python3
"""
Clean a conda environment.yml exported from another OS.

For the uploaded file, the real project packages are in the pip: section.
The conda section mostly contains Mac-specific/low-level solver packages.
This script therefore creates a portable Linux-friendly environment file with:

  - python=major.minor
  - pip
  - the original pip packages, unchanged

It also removes:
  - platform-specific conda build strings
  - macOS-only packages such as libcxx
  - low-level runtime libraries such as openssl, sqlite, zlib, etc.
  - the local prefix path, e.g. /anaconda3/envs/...

Usage:
    python clean_conda_env.py
    python clean_conda_env.py environment.yml environment_clean.yml
"""

from pathlib import Path
import re
import sys

input_file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("environment.yml")
output_file = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("environment_clean.yml")

if not input_file.exists():
    raise FileNotFoundError("Could not find: %s" % input_file)

lines = input_file.read_text().splitlines()

# --------
# 1. Read environment name
# --------
name = "clean_env"
for line in lines:
    m = re.match(r"^name:\s*(.+?)\s*$", line)
    if m:
        name = m.group(1)
        break

# --------
# 2. Read channels. If none are found, use defaults.
# --------
channels = []
in_channels = False
for line in lines:
    stripped = line.strip()
    if stripped == "channels:":
        in_channels = True
        continue
    if in_channels:
        if re.match(r"^\s*-\s*", line):
            channels.append(re.sub(r"^\s*-\s*", "", line).strip())
        elif stripped:
            break

if not channels:
    channels = ["defaults"]

# De-duplicate channels while preserving order.
seen = set()
channels = [c for c in channels if not (c in seen or seen.add(c))]

# --------
# 3. Extract Python version from conda dependencies.
#    Convert python=3.10.4=some_build -> python=3.10
# --------
python_version = "3.10"
for line in lines:
    m = re.match(r"^\s*-\s*python(?:={1,2})(\d+\.\d+)(?:\.\d+)?(?:=.*)?\s*$", line)
    if m:
        python_version = m.group(1)
        break

# --------
# 4. Extract pip packages exactly as they are.
# --------
pip_packages = []
in_pip = False
pip_indent = None

for line in lines:
    if re.match(r"^\s*-\s*pip:\s*$", line):
        in_pip = True
        pip_indent = len(line) - len(line.lstrip())
        continue

    if in_pip:
        stripped = line.strip()

        # Blank lines inside pip section: keep them.
        if stripped == "":
            pip_packages.append("")
            continue

        current_indent = len(line) - len(line.lstrip())

        # pip package lines are more indented than the '- pip:' line.
        if current_indent > pip_indent and re.match(r"^\s*-\s*", line):
            package = re.sub(r"^\s*-\s*", "", line).rstrip()
            pip_packages.append(package)
            continue

        # We reached the next conda dependency or another YAML section.
        in_pip = False

# --------
# 5. Build a new portable environment file.
# --------
out = []
out.append("name: %s" % name)
out.append("channels:")
for ch in channels:
    out.append("  - %s" % ch)
out.append("dependencies:")
out.append("  - python=%s" % python_version)
out.append("  - pip")

if pip_packages:
    out.append("  - pip:")
    for pkg in pip_packages:
        if pkg == "":
            out.append("")
        else:
            out.append("    - %s" % pkg)

output_file.write_text("\n".join(out).rstrip() + "\n")

# --------
# 6. Report what was done.
# --------
print("Created cleaned environment file: %s" % output_file)
print("")
print("Kept as conda dependencies:")
print("  - python=%s" % python_version)
print("  - pip")
print("")
print("Kept %d pip packages unchanged." % len([p for p in pip_packages if p]))
print("")
print("Removed from the recreated file:")
print("  - macOS-only package(s), e.g. libcxx")
print("  - macOS build strings, e.g. hecd8cb5_0, hca72f7f_1")
print("  - low-level conda runtime libraries, e.g. openssl, sqlite, zlib")
print("  - local prefix path, e.g. /anaconda3/envs/...")
print("")
print("Now run:")
print("conda env create -f %s" % output_file)
