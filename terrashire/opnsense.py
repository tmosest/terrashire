import typer

from .mod import Mod

def opnsense_cmd_callback(value: str):
    if value != "init": # or value != "add":
        raise typer.BadParameter("Can only init at the moment")
    return value

class OpnSenseMod(Mod):
    def __init__(self):
        self.mod = "opnsense"

    def init(self):
        self.init_mod()
