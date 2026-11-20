# AutoFile Organizer & Workflow Utility

A lightweight, open-source Python CLI tool designed to automatically organize directories, batch-rename files, and streamline repetitive local file-management workflows.

## Features
- **Smart Categorization**: Automatically sorts files into structured folders (Documents, Images, Audio, Video, Code, Archives) based on extensions.
- **Dry-Run Mode**: Preview file movements before applying changes to prevent accidental overwrites.
- **Custom Rules**: Easily extendable extension mapping via clean Python dictionaries.
- **Zero External Dependencies**: Built purely on Python's standard library (`os`, `shutil`, `pathlib`, `argparse`).

## Usage

```bash
# Preview changes without moving files
python organizer.py /path/to/folder --dry-run

# Organize files in the target directory
python organizer.py /path/to/folder
