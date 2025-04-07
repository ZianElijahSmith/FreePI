#!/usr/bin/env python3
"""
FreePi Index Generator
Copyright: Zian Elijah Smith, 2025
License: GPL-3.0
Generates a free software package index from PyPI metadata.
"""

import requests
import json
from bs4 import BeautifulSoup
from pathlib import Path

# Free software licenses (expand as needed)
FREE_LICENSES = {
    "MIT License": True,
    "Apache License 2.0": True,
    "GNU General Public License v3 (GPLv3)": True,
    "GNU Lesser General Public License v3 (LGPLv3)": True,
    # Add more from GNU/OSI lists
}

# Output directory for the index
INDEX_DIR = Path("/home/gnunix/FreePI/index")
INDEX_DIR.mkdir(parents=True, exist_ok=True)

def get_all_packages():
    """Fetch the list of all PyPI packages from the simple API."""
    response = requests.get("https://pypi.org/simple/")
    soup = BeautifulSoup(response.text, "html.parser")
    packages = [a.text for a in soup.find_all("a")]
    return packages

def get_package_info(package_name):
    """Fetch metadata for a single package."""
    url = f"https://pypi.org/pypi/{package_name}/json"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching {package_name}: {e}")
        return None

def is_free_software(license_str):
    """Check if a license string matches a known free software license."""
    if not license_str:
        return False
    license_str = license_str.strip()
    return license_str in FREE_LICENSES or any(l in license_str for l in FREE_LICENSES)

def generate_index():
    """Generate the FreePi package index."""
    packages = get_all_packages()
    free_packages = {}

    for package in packages[:100]:  # Limit for testing; remove for full run
        print(f"Checking {package}...")
        info = get_package_info(package)
        if not info or "info" not in info:
            continue
        
        license_str = info["info"].get("license", "")
        if is_free_software(license_str):
            free_packages[package] = {
                "version": info["info"]["version"],
                "license": license_str,
                "releases": info["releases"],
            }

    # Write the simple index
    simple_index = INDEX_DIR / "simple"
    simple_index.mkdir(exist_ok=True)
    with open(simple_index / "index.html", "w") as f:
        f.write("<html><body>\n")
        for package in free_packages:
            f.write(f'<a href="{package}/">{package}</a><br>\n')
            # Write package subpage
            package_dir = simple_index / package
            package_dir.mkdir(exist_ok=True)
            with open(package_dir / "index.html", "w") as pf:
                pf.write(f"<html><body><h1>{package}</h1>\n")
                for version, files in free_packages[package]["releases"].items():
                    for file in files:
                        url = file["url"]
                        pf.write(f'<a href="{url}">{file["filename"]}</a><br>\n')
                pf.write("</body></html>")
        f.write("</body></html>")

    # Save metadata for reference
    with open(INDEX_DIR / "free_packages.json", "w") as f:
        json.dump(free_packages, f, indent=2)

if __name__ == "__main__":
    generate_index()
