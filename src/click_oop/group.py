from __future__ import annotations

from typing import TYPE_CHECKING

import click

if TYPE_CHECKING:
    from click_oop.command import BaseCommand


class Group(click.Group):
    def add_command_cls(self, cmd_cls: type[BaseCommand], name: str | None = None):
        cmd = cmd_cls.to_command()
        self.add_command(cmd, name=name)

    def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)
