import itertools

import pytest

from tests.utils import run_cli


def test_cli_help():
    stdout = run_cli("--help")
    assert "Commands:" in stdout


def test_required_option():
    with pytest.raises(RuntimeError) as e:
        run_cli("greet")
        assert "Missing option '--name'" in str(e.value)


def test_option_with_default():
    stdout = run_cli("greet --name John")
    assert "John" in stdout
    assert "USA" in stdout


@pytest.mark.parametrize(
    "name,birth_place", itertools.product(["Alice", "Bob"], ["UK", "Germany"])
)
def test_option_with_value(name: str, birth_place: str):
    stdout = run_cli(f"greet --name {name} -b {birth_place}")
    assert name in stdout
    assert birth_place in stdout
