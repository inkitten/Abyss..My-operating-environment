from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.style import Style

console = Console()

VERSION = "0.2.0"


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


def bullet_list(items, symbol="•"):
    return "\n".join(f"{symbol} {item}" for item in items)


def start_screen():
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
        "Integrate Tasks module into Abyss",
    ]

    changes = [
        "Startup screen",
        "Rich integration",
        "Working on Tasks module",
    ]

    console.print()

    console.print(
        panel_creator(
            f"{title}\n{subtitle}",
            f"[bold red1]ABYSS v{VERSION}",
            text_align="center",
        )
    )

    console.print(
        panel_creator(
            f"[bold]Current Mission[/]\n{bullet_list(missions)}",
            "[bold red1]MISSION[/]",
        )
    )

    console.print(
        panel_creator(
            bullet_list(changes, "✓"),
            "[bold red1]CHANGES[/]",
        )
    )


if __name__ == "__main__":
    start_screen()
