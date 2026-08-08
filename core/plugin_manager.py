import importlib
import pathlib as pl

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


def load_plugins(
    plugins_dir=PLUGINS_ROOT,
    load_externals=True,
    commands=DEFAULT_COMMANDS,
):
    """
    Find built-in plugins and register their commands.

    Each plugin must provide a register() function that
    returns its command information.
    """

    internal_plugins = plugins_dir / "internals"
    external_plugins = plugins_dir / "external"

    # Load built-in plugins.
    for plugin in internal_plugins.glob("*"):
        if not plugin.is_dir():
            continue

        module = importlib.import_module(f"plugins.internals.{plugin.name}.main")

        plugin_info = module.register()

        try:
            commands.update(plugin_info["commands"])
        except KeyError:
            print(f"No commands available in plugin: {plugin.name}")

    # External plugins will be implemented later.
    if load_externals:
        for plugin in external_plugins.glob("*"):
            pass

    return commands


def run_command(command):
    """Find and execute a registered Abyss command."""
    try:
        COMMANDS[command]()
    except KeyError:
        print("Command doesn't exist")


# Build the command registry when the command system is loaded.
COMMANDS = load_plugins()
