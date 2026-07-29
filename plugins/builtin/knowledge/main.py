import pathlib as pl

import toml


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
        with open("./plugins/builtin/knowledge/config.toml", "r") as file:
            return toml.load(file)
    except FileNotFoundError:
        print("Configuration file not found.")
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
    except FileExistsError:
        print("Note already exists.")


def remove_note(notes_dir: pl.Path, note_name: str):
    """
    Delete a markdown note.
    """
    note_path = get_note_path(notes_dir, note_name)

    try:
        note_path.unlink()
        print(f"Deleted '{note_name}'.")
    except FileNotFoundError:
        print("Note does not exist.")


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
    config = load_config()

    if config is None:
        return

    notes_root = config["main"].get("path")

    if not notes_root:
        print("Please enter a path for notes.")
        notes_root = input("Path: ").strip()

        config["main"]["path"] = notes_root

        with open("./plugins/builtin/knowledge/config.toml", "w") as file:
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
            break

        else:
            print("Please choose a valid option.\n")


if __name__ == "__main__":
    main()
