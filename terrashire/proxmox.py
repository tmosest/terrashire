import typer

from .mod import Mod

def proxmox_cmd_callback(value: str):
    if value != "init": # or value != "add":
        raise typer.BadParameter("Can only init at the moment")
    return value

class ProxmoxMod(Mod):
    def __init__(self):
        self.mod = "proxmox"

    def init(self):
        self.init_mod()
