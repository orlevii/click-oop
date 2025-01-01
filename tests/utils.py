import subprocess


def run_cmd(cmd: str) -> str:
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
    return out


def run_cli(args: str) -> str:
    return run_cmd(f"python -m tests.dummy_cli.main {args}")
