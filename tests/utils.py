from __future__ import annotations

import subprocess
from typing import Literal, overload


def run_cmd(cmd: str) -> tuple[str, str]:
    p = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    out, err = p.communicate()
    if p.returncode != 0:
        raise RuntimeError(f"Command failed: {cmd!r}\n{err}")
    return out, err


@overload
def run_cli(args: str, stderr: Literal[False] = False) -> str:
    pass


@overload
def run_cli(args: str, stderr: Literal[True]) -> tuple[str, str]:
    pass


def run_cli(args: str, stderr: bool = False) -> str | tuple[str, str]:
    out, err = run_cmd(f"python -m tests.dummy_cli.main {args}")
    if stderr:
        return out, err
    return out
