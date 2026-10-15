# Changelog

## 0.2.3 — 2026-10-15

Release branch: `main` (merged from `development`)

Stability release: the bug-fix pass planned in
[`DEBUG_TODO.md`](DEBUG_TODO.md). No new features.

### Fixed

- Blank input no longer crashes the REPL (`IndexError`); input is now parsed
  with `strip().split()` and empty lines are skipped
- `Ctrl+C` / `Ctrl+D` at the prompt exit cleanly instead of printing a
  traceback
- All arguments after the command name are forwarded to the command
  (`choice[1:]`) instead of only the first; `help` rejects more than one
  module name with a message
- `help tasks` works: the task plugin folder was renamed from `ToDo` to
  `tasks` so the folder name matches the registered module name
- Deleting a non-existent task ID now reports "Invalid ID" and asks again
  instead of claiming "Task deleted."
- Version is read from package metadata (`importlib.metadata`), so the CLI
  banner and help panel now match `pyproject.toml`; shows `dev` when not
  installed

### Changed

- Install and run with `pip install -e .` and the `Abyss` command
- New `core/ui.py` (shared `console` and `panel_creator`) and
  `core/version.py`, removing the `plugin_manager` ↔ `cli` circular import
- Task plugin imports `database` explicitly (`from . import database`)
  instead of `from .database import *`
- `.gitignore` now covers Obsidian workspace state and agent tool state;
  `docs/.obsidian/workspace.json` is no longer tracked

### Removed

- `main.py` and `requirements.txt` (superseded by the `Abyss` console script
  and `pyproject.toml`)
- `py-modules = ["main"]` from `pyproject.toml`
- The task plugin's stale `README.md` and `requirements.txt`

### Known Issues

- `core/cli.py` uses `except EOFError, KeyboardInterrupt:` and therefore
  needs Python 3.14+, while `pyproject.toml` still declares `>= 3.8`
- Plugins are located relative to the source tree: use `pip install -e .`;
  a regular install does not find them
- `Ctrl+C` / `Ctrl+D` inside the `tasks` and `notes` menus are not handled yet
- `tasks` / `notes` accept no arguments; typing extra words after them
  raises a `TypeError`
- Remaining hygiene items are listed in [`DEBUG_TODO.md`](DEBUG_TODO.md)

## 0.2.2 — 2026-10-01

Release branch: `main` (merged from `development`)

### Added

- Initial CLI
- Logger
- Notes plugin
- Dynamic plugin manager
- Task manager
- Module-specific help (`help <module>`)
- `docs/DEBUG_TODO.md` — known-bug list, the target of v0.2.3

### Changed

- Command-line executable style
- README corrected: working `help` examples, project structure, new
  "Known Issues" section pointing at the debug list

### Fixed

- Restored the missing `main.py` entry point (was referenced by the README
  and `pyproject.toml` but absent from the repository)
- Removed a stray SQLite database file (`x`) from the repository root

### Known Issues

- Several known bugs remain (blank-input crash, dropped CLI arguments,
  version mismatch, plugin path resolution after install, ...).
  The full list lives in [`DEBUG_TODO.md`](DEBUG_TODO.md) and is scheduled
  for v0.2.3. The banner version in `core/cli.py` still reads 0.3.0 — this
  is one of the listed bugs, intentionally not patched in a docs-only release.

## 0.2.1 — 2026-07

- Path fixes for plugins
- Documentation pass (installation, philosophy, changelog)

## 0.2.0 — 2026-07

- Logging added to modules
- Task manager integrated as the first Abyss plugin
