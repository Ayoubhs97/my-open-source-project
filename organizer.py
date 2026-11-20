import argparse
import shutil
from pathlib import Path

EXTENSION_MAP = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
    "Documents": {".pdf", ".docx", ".txt", ".xlsx", ".csv", ".md"},
    "Audio": {".mp3", ".wav", ".flac", ".aac", ".ogg"},
    "Video": {".mp4", ".mov", ".avi", ".mkv"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Code": {".py", ".js", ".html", ".css", ".json", ".sh"},
}


def get_category(extension: str) -> str:
    ext = extension.lower()
    for category, extensions in EXTENSION_MAP.items():
        if ext in extensions:
            return category
    return "Other"


def organize_directory(target_dir: Path, dry_run: bool = False) -> None:
    if not target_dir.exists() or not target_dir.is_dir():
        raise ValueError(f"Invalid directory: {target_dir}")

    for item in target_dir.iterdir():
        if item.is_file() and not item.name.startswith("."):
            category = get_category(item.suffix)
            dest_folder = target_dir / category
            dest_path = dest_folder / item.name

            if dry_run:
                print(f"[DRY-RUN] Would move: {item.name} -> {category}/")
            else:
                dest_folder.mkdir(exist_ok=True)
                shutil.move(str(item), str(dest_path))
                print(f"Moved: {item.name} -> {category}/")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Automatically organize files in a folder by category."
    )
    parser.add_argument("directory", type=str, help="Path to the target directory")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate organization without moving files",
    )
    args = parser.parse_args()
    organize_directory(Path(args.directory), dry_run=args.dry_run)


if __name__ == "__main__":
    main()
