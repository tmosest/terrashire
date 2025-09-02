import os
import time
import subprocess
import typer
from typing_extensions import Annotated
# from watchdog.observers import Observer

# from .config import Config
# from .event import SyncEventHandler

class Terrashire():

    def __init__(self):
        # TODO
        # self.config = Config()
        pass

    def help(self):
        """
        Prints a help messsage
        """
        print("This program helps to generate and maintain a homelab")
        print("")
        print("")
        print("Lets get started with some helpful software")
        print("For creating USB bootable dirves download: https://etcher.balena.io/")
        print("For routing download and install on your router: https://opnsense.org/download/")
        print("For virtual machines download and install: https://www.proxmox.com/en/downloads")
        print("")
        print("")
        print("To learn more read about")
        print("https://nginxproxymanager.com/")
        print("")
        print("")
    
    def init(self, 
        path: Annotated[str, typer.Argument(help="The local file path for the repo")] = None):
        """
        Prints a help messsage
        """
        # Get the absolute path
        absolute_path = os.path.abspath(path)
        print(f"Initializing homelab iac in {absolute_path}")
        try:
            mdkir = subprocess.run(["mkdir", f"{absolute_path}"], capture_output=True, text=True, check=False)
            print(mdkir.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            print(f"Stderr: {e.stderr}")

        try:
            cd = subprocess.run(["cd", f"{absolute_path}"], capture_output=True, text=True, check=False)
            print(cd.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            print(f"Stderr: {e.stderr}")

        try: 
            git_init = subprocess.run(["git", "init", "."], cwd=absolute_path, capture_output=True, text=True, check=False)
            print(git_init.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            print(f"Stderr: {e.stderr}")

        init_path = os.path.join(os.path.dirname(__file__), 'init')
        print(f"Copying files from {init_path}")
        try: 
            cp_init = subprocess.run(["cp", f"{init_path}/.gitignore", f"{absolute_path}/"], capture_output=True, text=True, check=False)
            print(cp_init.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            print(f"Stderr: {e.stderr}")

    def run(self):
        print("TODO running some stuff")

    def opnsense(self, cmd: Annotated[str, typer.Argument(help="What command the service is doing")] = None):
        print("TODO running some opnsense stuff")

    def npm(self, cmd: Annotated[str, typer.Argument(help="What command the service is doing")] = None):
        print("TODO running some nginx proxy manager stuff stuff")
