from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.style import Style

console = Console()

VERSION = "0.1.0"


def panel_creator(item, header):
    """
    Create a styled Rich panel.

    Returns the Panel instead of printing it so
    the caller decides where and when to display it.
    """
    panel_style = Style(color="green3", bold=True, dim=True)

    return Panel(
        item,
        title=header,
        border_style=panel_style,
    )

def abyss_help():
    help_msg = Panel(
        Align.center(
            f"""Welcome to ABYSS v{VERSION}

ABYSS is my operation environment and playground.

Commands

1. help
2. exit
"""
        )
    )

    console.print(help_msg)

def start_screen():
    panel_style = Style(color="green3", bold=True, dim=True)

    title = Text(
        f"ABYSS v{VERSION}",
        style="bold green3",
        justify="center",
    )

    subtitle = Text(
        "Build • Learn • Explore",
        style="italic",
    )

    console.print()

    console.print(
        Panel(
            Align.center(title + "\n" + subtitle),
            border_style=panel_style,
            title="[bold red1]WELCOME[/]",
        )
    )

    missions = [
        "• Integrate Tasks module into Abyss",
    ]

    mission_text = "[bold]Current Mission[/]\n" + "\n".join(missions)

    console.print(
        panel_creator(
            mission_text,
            "[bold red1]MISSION[/]",
        )
    )

    console.print(
        panel_creator(
            "✓ Startup screen\n"
            "✓ Rich integration\n"
            "• Working on Tasks module",
            "[bold red1]CHANGES[/]",
        )
    )



if __name__ == "__main__":
    start_screen()