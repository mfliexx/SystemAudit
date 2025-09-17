# System-Audit is a simple Python CLI tool for performing a basic security audit of your system

## Features

1. Checks OS name and version
2. Checks system architecture and processor type
3. Checks Python version and compiler
4. Checks computer name and current user
5. Colorful console report
6. Optional CLI flags (--os, --python, --arch, --user)
7. Optionally saves the report to a file (`audit_report.txt`)

## Installation

Clone and install dependencies:
```bash
git clone https://github.com/mfliexx/SystemAudit.git
cd SystemAudit
pip install colorama pyfiglet

