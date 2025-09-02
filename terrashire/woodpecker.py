import typer

from .mod import Mod

def woodpecker_cmd_callback(value: str):
    if value != "init": # or value != "add":
        raise typer.BadParameter("Can only init at the moment")
    return value

class WoodpeckerMod(Mod):
    def __init__(self):
        self.mod = "woodpecker"

    def init(self):
        self.init_mod()
