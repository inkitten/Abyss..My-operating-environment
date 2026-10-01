# Debug TODO — v0.2.3

> Known bugs and defects found during the v0.2.2 review.
> Goal: fix all of these **before** adding any new features, and before the
> move to a `typer`-based CLI (planned for v0.3.0).

Legend: 🔴 crash / data risk · 🟠 wrong behavior · 🟡 hygiene / quality

---

## 🔴 Critical

- [ ] **Blank input crashes the REPL**
      `core/cli.py` — pressing Enter on an empty line raises `IndexError`:
      `"".split(" ")` → `[""]` → the removal loop empties the list → `choice[0]` fails.
      Fix: `choice = input("abyss:> ").strip().split()` and drop the whole
      `for _ in range(100)` cleanup loop.

- [ ] **`Ctrl+D` / `Ctrl+C` crash with a raw traceback**
      `input()` raises `EOFError` / `KeyboardInterrupt` which nothing catches —
      in the main loop and in every plugin menu (`ToDo`, `knowledge`).
      Fix: catch both at the REPL and exit (or re-prompt) gracefully.

- [ ] **Installed `Abyss` script can't find plugins**
      `core/plugin_manager.py` — `PLUGINS_ROOT` is derived from `__file__`, so a
      real `pip install .` looks for plugins inside site-packages and finds none.
      Fix: resolve plugins relative to the project root / configurable path.

## 🟠 Wrong behavior

- [ ] **`help ToDo` doesn't work**
      The README advertised it; the module registers under the name `tasks`.
      Either match folder names as a fallback in `abyss_help`, or make
      registered name == folder name.

- [ ] **Extra command arguments are silently dropped**
      `run_command(choice[0], choice[1])` throws away everything after the
      second token. The planned `notes add` / `notes remove` subcommands need
      the full list: pass `choice[1:]`.

- [ ] **`delete_task` claims success even when nothing was deleted**
      `plugins/internals/ToDo/main.py` prints "Task deleted." regardless of
      whether the ID existed. Check `c.rowcount` in `delete_task_db`.

- [ ] **Version mismatch in three places**
      `pyproject.toml` = 0.2.1, `core/cli.py` VERSION = 0.3.0, CHANGELOG = 0.3.0.
      Single source of truth: read the version via
      `importlib.metadata.version("Abyss")` (fallback constant when not installed).

- [ ] **Tag search matches substrings**
      `database.py` `search_by_tag_db` uses `LIKE '%tag%'` — searching "work"
      also matches "network". Strip `%`/`_` from input, or store/compare tags
      as separate tokens.

## 🟡 Hygiene / quality

- [ ] **`from .database import *` in the ToDo plugin**
      `main()` uses `conn` that it never imported — it only works through the
      star import. Replace with `from . import database` and give the DB layer
      an explicit `close()` function.

- [ ] **Import-time side effects**
      `database.py` opens SQLite and creates tables at import; `plugin_manager.py`
      runs `load_plugins()` at import. Move initialization into functions called
      explicitly — required before tests are possible.

- [ ] **Circular import worked around instead of fixed**
      `plugin_manager` ↔ `cli` works only because of a function-body import.
      Move `panel_creator` / `console` into a `core/ui.py` so the cycle dies.

- [ ] **Plugin command name collisions are silent**
      `commands.update(...)` overwrites duplicates without warning. Log a
      warning when a plugin registers a name that already exists.

- [ ] **Mixed output primitives**
      Some paths use `print()`, others `console.print()`. Standardize on the
      rich console for consistent styling.

- [ ] **Variable shadowing in `show_tasks`**
      `for row in rows: task_id, title, date, ...` shadows the `datetime.date`
      import. Rename to `created`.

- [ ] **Cancelled ID prompts trap the user**
      `complete_task` / `delete_task` loop forever on bad input; empty input
      should abort back to the menu.

- [ ] **Repo hygiene**
      Remove the stray SQLite file `x` at the repo root (done in v0.2.2) and
      make sure `*.db` artifacts can never be committed again.

---

## Verification checklist for 0.2.3

- [ ] `python main.py` starts; pressing Enter on an empty prompt does nothing harmful
- [ ] `Ctrl+D` at the prompt exits cleanly with a goodbye message
- [ ] `help`, `help tasks` (and folder-name fallback) all work
- [ ] `tasks add a b c` style multi-word input no longer loses arguments
- [ ] Deleting a nonexistent ID reports failure, not success
- [ ] `pip install .` then running the `Abyss` script still discovers plugins
- [ ] Version is identical in `pyproject.toml`, the CLI banner, and the CHANGELOG
