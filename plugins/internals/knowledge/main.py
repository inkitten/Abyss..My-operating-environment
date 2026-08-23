import pathlib as pl
from core.logger import get_logger
import toml

logger = get_logger(__name__)
config_file = pl.Path(__file__) / "config.toml"

# =============================================================================
# Configuration
# =============================================================================
def load_config():
    """
    Load the Notes module configuration.

    Returns:
        dict | None: Parsed TOML configuration or None if the file is missing.
    """
    try:
        with open(config_file, "r") as file:
            logger.info("Notes configuration loaded")
            return toml.load(file)
    except FileNotFoundError:
        print("Configuration file not found.")
        logger.error("Notes configuration file not found")
        return None


# =============================================================================
# Helpers
# =============================================================================
def get_note_path(notes_dir: pl.Path, note_name: str) -> pl.Path:
    """
    Return the full path of a note.

    Example:
        Notes + "Meeting"
            -> ~/Abyss_notes/Meeting.md
    """
    return notes_dir / f"{note_name}.md"


# =============================================================================
# Note Operations
# =============================================================================
def add_note(notes_dir: pl.Path, note_name: str):
    """
    Create a new markdown note.
    """
    note_path = get_note_path(notes_dir, note_name)

    try:
        note_path.touch(exist_ok=False)
        print(f"Created '{note_name}'.")
        logger.info("Created note: %s", note_name)
    except FileExistsError:
        print("Note already exists.")
        logger.warning("Attempted to create existing note: %s", note_name)


def remove_note(notes_dir: pl.Path, note_name: str):
    """
    Delete a markdown note.
    """
    note_path = get_note_path(notes_dir, note_name)

    try:
        note_path.unlink()
        print(f"Deleted '{note_name}'.")
        logger.info("Deleted note: %s", note_name)
    except FileNotFoundError:
        print("Note does not exist.")
        logger.warning("Attempted to delete nonexistent note: %s", note_name)


def view_notes(notes_dir: pl.Path):
    """
    List all available notes.
    """
    notes = sorted(notes_dir.glob("*.md"))

    if not notes:
        print("No notes found.\n")
        return

    print("\nAvailable Notes:\n")

    for note in notes:
        print(f"- {note.stem}")

    print()


# =============================================================================
# CLI
# =============================================================================
def main():
    logger.info("Notes module started")
    config = load_config()

    if config is None:
        logger.error("Notes module stopped: configuration unavailable")
        return

    notes_root = config["main"].get("path")

    if not notes_root:
        print("Please enter a path for notes.")
        notes_root = input("Path: ").strip()

        config["main"]["path"] = notes_root

        with open(config_file, "w") as file:
            toml.dump(config, file)

    notes_dir = pl.Path(notes_root) / "Abyss_notes"
    notes_dir.mkdir(exist_ok=True)

    menu = """
Welcome to Notes

1. Add Note
2. Remove Note
3. View Notes
4. Exit
"""

    while True:
        print(menu)

        choice = input("> ").strip()

        if choice == "1":
            add_note(notes_dir, input("Note name: ").strip())

        elif choice == "2":
            remove_note(notes_dir, input("Note name: ").strip())

        elif choice == "3":
            view_notes(notes_dir)

        elif choice == "4":
            print("Thank you for using the Notes module.")
            logger.info("Notes module exited")
            break

        else:
            print("Please choose a valid option.\n")


def register():
    return {
        "name": "notes",
        "version": "0.1.0",
        "author": "inkitten",
        "description": "Knowledge management",
        "commands": {
            "notes": main,
            # Will be added in the future.
            # "notes add": add_note,
            # "notes remove": remove_note,
        },
    }


if __name__ == "__main__":
    main()
