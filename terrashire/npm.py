import typer

from .mod import Mod

def npm_cmd_callback(value: str):
    if value != "init": # or value != "add":
        raise typer.BadParameter("Can only init at the moment")
    return value

class NpmMod(Mod):
    def __init__(self):
        self.mod = "npm"

    def init(self):
        self.init_mod()
