from typing import Annotated

from pydantic import BaseModel

from click_oop import BaseCommand, Option, OptionSettings


class GreetCommandParams(BaseModel):
    name: Option[str]
    birth_place: Annotated[str, OptionSettings(aliases=["-b"])] = "USA"


class GreetCommand(BaseCommand[GreetCommandParams]):
    NAME = "greet"

    def run(self):
        print("Hello,", self.params.name, "from", self.params.birth_place)
