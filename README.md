# SwiftCLI
Build testable CLI apps with `click` and `pydantic`

`swiftcli` makes it easy to define cli parameters with a `pydantic` BaseModel

## Simple CLI
```python
from pydantic import BaseModel

from swiftcli import BaseCommand, Group
from swiftcli.types import Argument, Option


class GreetParams(BaseModel):
    name: Argument[str]  # required argument
    color: Option[str] = ""  # Optional --color option with default value


class GreetCommand(BaseCommand[GreetParams]):
    NAME = "greet"

    def run(self) -> None:
        if self.params.color:
            print(f"Hello, {self.params.name}. You like the color {self.params.color}.")
        else:
            print(f"Hello, {self.params.name}.")


cli = Group()
cli.add_command_cls(GreetCommand)

if __name__ == "__main__":
    cli()
```

## Simple Types
`swiftcli` implements simple types like:
* Argument - <fill>
* Option - <fill>
* Flag - <fill>
* Switch - <fill>
