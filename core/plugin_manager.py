from core.logger import get_logger
import importlib.util as util
import pathlib as pl
import sys

logger = get_logger(__name__)

from core.cli import panel_creator, console, VERSION

# Root directory containing Abyss plugins.
PLUGINS_ROOT = pl.Path(__file__).parent.parent / "plugins"


def abyss_help():
    """Display available Abyss commands."""
    console.print(
        panel_creator(
            f"""Welcome to ABYSS v{VERSION}

ABYSS is my operation environment and playground.

Available Commands

{"\n".join(COMMANDS.keys())}
""",
            "Abyss Help",
            text_align="center",
        )
    )


# Commands that belong to Abyss itself rather than a plugin.
DEFAULT_COMMANDS = {
    "options": abyss_help,
    "help": abyss_help,
}


def load_module_from_path(module_name, dir_path, file_path):
    spec = util.spec_from_file_location(
        module_name, location=file_path, submodule_search_locations=[str(dir_path)]
    )
    module = util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_plugins(
    plugins_dir=PLUGINS_ROOT,
    load_externals=True,
    commands=None,
):
    """
    Find built-in plugins and register their commands.

    Each plugin must provide a register() function that
    returns its command information.
    """
    if not commands:
        commands = dict(DEFAULT_COMMANDS)

    for t in plugins_dir.glob("*"):
        if not t.is_dir() or t.name[0] in "_-.$@":
            continue
        plugin_type = t.name

        for p in t.glob("*"):
            if not p.is_dir() or p.name[0] in "_-.$@":
                continue
            plugin_name = p.name
            try:
                module = load_module_from_path(plugin_name, p, p / "main.py")
                register = getattr(module, "register")
                module_state = register()
                commands.update(module_state["commands"])
            except Exception as e:
                logger.error(f"Unable to load {plugin_name}: {e}")
                print(f"Unable to add {plugin_name} plugin")
    return commands


def run_command(command):
    """Find and execute a registered Abyss command."""
    try:
        COMMANDS[command]()
    except KeyError:
        print("Command doesn't exist")


# Build the command registry when the command system is loaded.
COMMANDS = load_plugins()
