# Changelog

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
