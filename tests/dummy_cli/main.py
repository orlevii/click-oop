from click_oop import Group
from tests.dummy_cli.commands.greet import GreetCommand

cli = Group()
cli.add_command_cls(GreetCommand)

if __name__ == "__main__":
    cli()
