from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.style import Style

console = Console()

VERSION = "0.1.0"


def panel_creator(
    item,
    header,
    text_align="left",
    panel_align=None,
):
    panel_style = Style(color="green3", bold=True, dim=True)

    panel = Panel(
        Align(item, align=text_align),
        title=header,
        border_style=panel_style,
    )

    if panel_align:
        return Align(panel, align=panel_align)

    return panel


def abyss_help():
    console.print(
        panel_creator(f"""Welcome to ABYSS v{VERSION}

    ABYSS is my operation environment and playground.

    Available Commands

    1. help
    2. exit
    ""","Abyss help", text_align="center"))



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

    missions = [
        "• Integrate Tasks module into Abyss",
    ]

    mission_text = "[bold]Current Mission[/]\n" + "\n".join(missions)

    console.print()

    console.print(
        panel_creator(f"{title}\n{subtitle}", f"[bold red1]ABYSS v{VERSION}", text_align="center")
    )

    console.print(
        panel_creator(
            mission_text,
            "[bold red1]MISSION[/]",
        )
    )

    console.print(
        panel_creator(
            "✓ Startup screen\n" "✓ Rich integration\n" "• Working on Tasks module",
            "[bold red1]CHANGES[/]",
        )
    )


if __name__ == "__main__":
    start_screen()
