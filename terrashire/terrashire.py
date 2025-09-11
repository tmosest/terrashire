import os
import pprint
import time
import typer
from typing_extensions import Annotated
# from watchdog.observers import Observer

# from .config import Config
# from .event import SyncEventHandler
from .cmd_util import copy, run
from .gitea import gitea_cmd_callback, GiteaMod
from .help import help
from .mod import Mod
from .network import detect_new_devices, scan_network
from .npm import npm_cmd_callback, NpmMod
from .opnsense import opnsense_cmd_callback, OpnSenseMod
from .pihole import pihold_cmd_callback, PiHoleMod
from .proxmox import proxmox_cmd_callback, ProxmoxMod
from .woodpecker import woodpecker_cmd_callback, WoodpeckerMod

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

        print(f"Initializing new git repo at {absolute_path}")
        run(f"rm __init__.py", absolute_path)
        # TODO this isn't working...
        run(f"rm  -R -f __pycache__", absolute_path)
        run(f"rm  -R -f __pycache__", absolute_path)

        run(f"mv Config.json .Config.json", absolute_path)

        run("git init .", absolute_path)
        run("ls -l -a", absolute_path)
        print("Done initializing")
    

    def list_network(self, target_ip_range="192.168.1.1/24"):
        pprint.pprint(scan_network(target_ip_range))

    def detect_new_devices(self, target_ip_range="192.168.1.1/24"):
         pprint.pprint(detect_new_devices(target_ip_range))

    def run(self):
        print("TODO running some stuff")

    def run_mod(self, cmd, mod : Mod):
        print(f"Running {mod} {cmd}")
        if cmd == "init":
            mod.init()

    # MODs
    def gitea(self, cmd: Annotated[str, typer.Argument(help="init", callback=gitea_cmd_callback)] = None):
        mod = GiteaMod()
        self.run_mod(cmd=cmd, mod=mod)
    
    def opnsense(self, cmd: Annotated[str, typer.Argument(help="init", callback=opnsense_cmd_callback)] = None):
        mod = OpnSenseMod()
        self.run_mod(cmd=cmd, mod=mod)
    
    def pihole(self, cmd: Annotated[str, typer.Argument(help="init", callback=pihold_cmd_callback)] = None):
        mod = PiHoleMod()
        self.run_mod(cmd=cmd, mod=mod)

    def npm(self, cmd: Annotated[str, typer.Argument(help="init", callback=npm_cmd_callback)] = None):
        mod = NpmMod()
        self.run_mod(cmd=cmd, mod=mod)
    
    def proxmox(self, cmd: Annotated[str, typer.Argument(help="init", callback=proxmox_cmd_callback)] = None):
        mod = ProxmoxMod()
        self.run_mod(cmd=cmd, mod=mod)
    
    def woodpecker(self, cmd: Annotated[str, typer.Argument(help="init", callback=woodpecker_cmd_callback)] = None):
        mod = WoodpeckerMod()
        self.run_mod(cmd=cmd, mod=mod)
