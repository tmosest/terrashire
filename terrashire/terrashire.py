import os
import time
import typer
from typing_extensions import Annotated
# from watchdog.observers import Observer

# from .config import Config
# from .event import SyncEventHandler
from .help import help
from .cmd_util import copy, run

class Terrashire():

    def __init__(self):
        # TODO
        # self.config = Config()
        pass

    def help(self):
        return help()
    
    def init(self, 
        path: Annotated[str, typer.Argument(help="The local file path for the repo")] = None):
        """
        Prints a help messsage
        """
        # Get the absolute path
        absolute_path = os.path.abspath(path)
        print(f"Initializing homelab iac in {absolute_path}")

        init_path = os.path.join(os.path.dirname(__file__), 'init')
        print(f"Copying files from {init_path}")
        copy(init_path, absolute_path)
        run("git init .")

    def init_mod(self, mod: str):
        absolute_path = os.getcwd()
        repo_path = os.path.join(absolute_path, mod)
        package_path = os.path.join(os.path.dirname(__file__), mod)
        print(f"Copying files from {package_path} to {repo_path}")
            
        try: 
            copy(package_path, repo_path)
        except Exception as e:
            print(f"Error executing command: {e}")

    def run(self):
        print("TODO running some stuff")

    def run_mod(self, cmd, mod):
        print(f"Running {mod} {cmd}")
        if cmd == "init":
            self.init_mod(mod)

    # MODs
    def opnsense_cmd_callback(value: str):
        if value != "init": # or value != "add":
            raise typer.BadParameter("Can only init at the moment")
        return value
    
    def opnsense(self, cmd: Annotated[str, typer.Argument(help="init", callback=opnsense_cmd_callback)] = None):
        mod = 'opnsense'
        self.run_mod(cmd=cmd, mod=mod)

    def pihold_cmd_callback(value: str):
        if value != "init": # or value != "add":
            raise typer.BadParameter("Can only init at the moment")
        return value
    
    def pihole(self, cmd: Annotated[str, typer.Argument(help="init", callback=pihold_cmd_callback)] = None):
        mod = 'pihole'
        self.run_mod(cmd=cmd, mod=mod)

    def npm_cmd_callback(value: str):
        if value != "init": # or value != "add":
            raise typer.BadParameter("Can only init at the moment")
        return value

    def npm(self, cmd: Annotated[str, typer.Argument(help="init", callback=npm_cmd_callback)] = None):
        mod = 'npm'
        self.run_mod(cmd=cmd, mod=mod)

    def proxmox_cmd_callback(value: str):
        if value != "init": # or value != "add":
            raise typer.BadParameter("Can only init at the moment")
        return value
    
    def proxmox(self, cmd: Annotated[str, typer.Argument(help="init", callback=proxmox_cmd_callback)] = None):
        mod = 'proxmox'
        self.run_mod(cmd=cmd, mod=mod)
