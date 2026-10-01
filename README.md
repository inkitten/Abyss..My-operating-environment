# Abyss

> A modular command-line playground for learning software engineering, Linux, networking, and cybersecurity through real projects.

Abyss is a personal playground for building, breaking, experimenting, and learning.

Instead of keeping every experiment as a separate unfinished project, Abyss provides a small environment where useful tools can eventually live as modules.

The project is intentionally developed in small steps. It is not designed to be perfect from the beginning.

## Current Status

🚧 **Early Development — v0.2.x**

Abyss currently provides:

- Interactive command-line interface
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
│   └── plugin_manager.py
│
├── plugins/
│   ├── internals/
│   │   ├── knowledge/
│   │   └── ToDo/
│   └── externals/
│
├── docs/
│   ├── CHANGELOG.md
│   ├── DEBUG_TODO.md
│   ├── PHILOSOPHY.md
│   └── ROADMAP.md
│
├── main.py
├── README.md
├── requirements.txt
└── pyproject.toml
```

## Installation

Clone the repository:

```bash
git clone https://github.com/inkitten/Abyss..My-operating-environment.git Abyss
cd Abyss
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Run Abyss:

```bash
python main.py
```

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
```

> [!NOTE]
> Module help uses the module's registered name, which may differ from its
> folder name (the task manager lives in `plugins/internals/ToDo/` but is
> registered as `tasks`).

## Known Issues

Abyss is a learning project in active development, and v0.2.2 ships with a
handful of known bugs (blank input crash, dropped CLI arguments, version
mismatch, and more).

The full list lives in [`docs/DEBUG_TODO.md`](docs/DEBUG_TODO.md) and is the
main target of the next release.

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
