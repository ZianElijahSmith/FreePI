#!/usr/bin/env python3
"""
FreePi Index Generator
Copyright: Zian Elijah Smith, 2025
License: GPL-3.0
Generates a free software package index from PyPI metadata.

Creates index.html and free_packages.json


"""

import requests
import json
import time
from bs4 import BeautifulSoup
from pathlib import Path

FREE_LICENSES = {
    "MIT": True, "MIT License": True,
    "Apache": True, "Apache License": True, "Apache License 2.0": True,
    "Apache 2": True, "Apache 2.0": True,
    "GPL": True, "GNU General Public License": True,
    "GNU General Public License v3": True, "GNU General Public License v3 (GPLv3)": True,
    "GPLv3": True, "GPL-3.0": True,
    "LGPL": True, "GNU Lesser General Public License": True,
    "GNU Lesser General Public License v3": True, "GNU Lesser General Public License v3 (LGPLv3)": True,
    "LGPLv3": True, "LGPL-3.0": True,
    "BSD": True, "BSD License": True,
    "ISC": True,
}

INDEX_DIR = Path("/home/gnunix/FreePI/index")
INDEX_DIR.mkdir(parents=True, exist_ok=True)

def get_all_packages():
    response = requests.get("https://pypi.org/simple/")
    soup = BeautifulSoup(response.text, "html.parser")
    packages = [a.text for a in soup.find_all("a")]
    return packages

def get_package_info(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    for attempt in range(3):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching {package_name} (attempt {attempt+1}): {e}")
            time.sleep(2 ** attempt)
    print(f"Failed to fetch {package_name} after 3 attempts")
    return None

def is_free_software(license_str):
    if not license_str:
        return False
    license_str = license_str.strip().lower()
    return license_str in FREE_LICENSES or any(l.lower() in license_str for l in FREE_LICENSES)

def generate_index():
    packages = get_all_packages()
    free_packages = {}
    print(f"Total packages to check: {len(packages)}")

    for package in packages:  # Full run
        print(f"Checking {package}...")
        info = get_package_info(package)
        if not info or "info" not in info:
            print(f"No info for {package}")
            continue
        
        license_str = info["info"].get("license", "")
        print(f"License for {package}: '{license_str}'")
        if is_free_software(license_str):
            print(f"Found free package: {package}")
            free_packages[package] = {
                "version": info["info"]["version"],
                "license": license_str,
                "releases": info["releases"],
            }
        time.sleep(0.1)  # Be polite to PyPI

    print(f"Total free packages found: {len(free_packages)}")
    if not free_packages:
        print("No free packages detected. Check license matching logic.")

    simple_index = INDEX_DIR / "simple"
    simple_index.mkdir(exist_ok=True)
    with open(simple_index / "index.html", "w") as f:
        f.write("<html><body>\n")
        for package in sorted(free_packages):
            f.write(f'<a href="{package}/">{package}</a><br>\n')
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

    with open(INDEX_DIR / "free_packages.json", "w") as f:
        json.dump(free_packages, f, indent=2)

if __name__ == "__main__":
    generate_index()
