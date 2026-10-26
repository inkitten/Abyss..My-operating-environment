# Abyss

> A modular command-line playground for learning software engineering, Linux, networking, and cybersecurity through real projects.

Abyss is a personal playground for building, breaking, experimenting, and learning.

Instead of keeping every experiment as a separate unfinished project, Abyss provides a small environment where useful tools can eventually live as modules.

The project is intentionally developed in small steps. It is not designed to be perfect from the beginning.

## Current Status

🚧 **Early Development — v0.2.3**

v0.2.3 is a stability release: it fixes the bugs found in the v0.2.2 review
and adds no new features. See [`docs/CHANGELOG.md`](docs/CHANGELOG.md).

Abyss currently provides:

- Interactive command-line interface (blank input is ignored, `Ctrl+C` /
  `Ctrl+D` exit cleanly)
- Dynamic plugin/module loading
- Built-in help system
- Module-specific help and descriptions
- Logging
- Notes / knowledge module
- Task management module
- Plugin-based architecture

The project is actively being developed and its architecture is expected to change.

## Philosophy

Abyss is a **playground, not a monument**.

The main goal is learning by building:

```text
Build
  ↓
Use
  ↓
Find a problem
  ↓
Understand
  ↓
Improve
```

Nothing should be added just because it seems useful someday. New functionality should solve a real problem or provide an intentional learning opportunity.

Abyss is also a way to keep the development journey visible through Git history, branches, releases, documentation, and experiments.

See [`docs/PHILOSOPHY.md`](docs/PHILOSOPHY.md) for the full philosophy.

## Project Structure

```text
Abyss/
├── core/
│   ├── cli.py
│   ├── logger.py
│   ├── plugin_manager.py
│   ├── ui.py
│   └── version.py
│
├── plugins/
│   ├── internals/
│   │   ├── knowledge/
│   │   └── tasks/
│   └── externals/
│
├── docs/
│   ├── CHANGELOG.md
│   ├── DEBUG_TODO.md
│   ├── PHILOSOPHY.md
│   └── ROADMAP.md
│
├── LICENSE
├── README.md
└── pyproject.toml
```

## Installation

Clone the repository:

```bash
git clone https://github.com/inkitten/Abyss..My-operating-environment.git Abyss
cd Abyss
```

Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

Install Abyss in editable mode (this also installs the dependencies):

```bash
python -m pip install -e .
```

> [!IMPORTANT]
> Install with `-e` (editable). Plugins are looked up relative to the source
> checkout, so a regular `pip install .` will not find them yet.

> [!NOTE]
> The CLI currently uses syntax that requires **Python 3.14 or newer**, even
> though `pyproject.toml` still declares `>= 3.12`. See
> [`docs/DEBUG_TODO.md`](docs/DEBUG_TODO.md).

Run Abyss:

```bash
Abyss
```

`requirements.txt` and `main.py` no longer exist; `Abyss` is the only entry
point.

## Commands

Abyss currently provides an interactive command interface.

```text
abyss:> help
```

Display available modules and built-in commands.

Module-specific help is also available:

```text
abyss:> help <module>
```

For example:

```text
abyss:> help tasks
abyss:> help notes
```

`help` accepts at most one module name. Module names match the plugin folder
names (`tasks` lives in `plugins/internals/tasks/`).

Other commands:

| Command     | What it does               |
| ----------- | -------------------------- |
| `tasks`     | Open the task manager menu |
| `notes`     | Open the notes menu        |
| `options`   | Same as `help`             |
| `q`, `exit` | Quit                       |

Blank lines are ignored. `Ctrl+C` and `Ctrl+D` also quit cleanly.
Everything typed after the command name is forwarded to the command as a
list (groundwork for subcommands such as `notes add`). The current `tasks` and
`notes` menus take no arguments yet, so run them without any.

## Known Issues

v0.2.3 fixed most of the bugs found in the v0.2.2 review. The ones still open
include:

- The CLI needs Python 3.14+ (an `except A, B:` clause), but `pyproject.toml`
  declares `>= 3.12`.
- `pip install .` (non-editable) can't find plugins; use `pip install -e .`.
- `Ctrl+C` / `Ctrl+D` inside the `tasks` and `notes` menus still show a
  traceback.
- Running `tasks` or `notes` with extra arguments (e.g. `tasks add`) crashes
  the REPL with a `TypeError`.
- Tag search in `tasks` matches substrings (`work` also matches `network`).

The full list lives in [`docs/DEBUG_TODO.md`](docs/DEBUG_TODO.md).

## Development

Abyss is primarily a learning project, so development happens incrementally.

Features are developed in branches and integrated into `development` before becoming part of a stable release.

The project may contain unfinished, experimental, or intentionally imperfect code. That is part of the process.

## Roadmap

The long-term direction is to gradually turn things learned in software engineering, Linux, networking, and cybersecurity into useful Abyss modules.

The general loop is:

```text
Learn a concept
      ↓
Practice it
      ↓
Understand the underlying system
      ↓
Build a small tool
      ↓
Integrate it into Abyss when useful
      ↓
Move to the next problem
```

See [`docs/ROADMAP.md`](docs/ROADMAP.md) for the current roadmap.

## License

MIT
