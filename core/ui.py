from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.style import Style

console = Console()


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
