from typing import Any

import click

from swiftcli import Group
from tests.dummy_cli.commands.greet import GreetCommand


def print_version(ctx: click.Context, _: Any, value: bool) -> None:
    if not value:
        return
    msg = "DummyCLI {}".format(click.style("0.1.0", fg="yellow"))
    click.echo(msg)
    ctx.exit()


cli = Group(
    params=[
        click.Option(
            ["--version", "-V"],
            is_flag=True,
            callback=print_version,
            help="Display realm version",
        )
    ]
)
cli.add_command_cls(GreetCommand)

if __name__ == "__main__":
    cli()
