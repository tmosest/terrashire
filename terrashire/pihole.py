import typer

from .mod import Mod

def pihold_cmd_callback(value: str):
    if value != "init": # or value != "add":
        raise typer.BadParameter("Can only init at the moment")
    return value

class PiHoleMod(Mod):
    def __init__(self):
        self.mod = "pihole"

    def init(self):
        self.init_mod()
