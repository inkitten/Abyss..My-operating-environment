from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.style import Style

console = Console()

VERSION = "0.3.0"


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
        "Adding API",
    ]

    changes = [
        "command-line executable style",
    ]

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


def main():
    start_screen()
    while True:

        choice = input("abyss:> ").split(" ")
        for _ in range(100):
            try:
                choice.remove("")
            except:
                pass
        if choice[0] in ["q", "exit"]:
            break

        from core.plugin_manager import run_command

        if len(choice) == 1:
            run_command(choice[0])
        elif len(choice) >= 2:
            run_command(choice[0], choice[1])

    print("Goodbye!")


if __name__ == "__main__":
    start_screen()
