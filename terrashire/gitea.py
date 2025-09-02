import typer

from .mod import Mod

def gitea_cmd_callback(value: str):
    if value != "init": # or value != "add":
        raise typer.BadParameter("Can only init at the moment")
    return value

class GiteaMod(Mod):
    def __init__(self):
        self.mod = "gitea"

    def init(self):
        self.init_mod()
