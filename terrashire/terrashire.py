import os
import time
import shutil
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
            shutil.copytree(init_path, absolute_path)
        except Exception as e:
            print(f"Error executing command: {e}")

    def run(self):
        print("TODO running some stuff")

    def opnsense_cmd_callback(value: str):
        if value != "init": # or value != "add":
            raise typer.BadParameter("Can only init at the moment")
        return value
    
    def opnsense(self, cmd: Annotated[str, typer.Argument(help="init", callback=opnsense_cmd_callback)] = None):
        print(f"Running opnsense {cmd}")
        
        if cmd == "init":
            absolute_path = os.getcwd()
            repo_opnsense_path = os.path.join(absolute_path, 'opnsense')
            package_opnsense_path = os.path.join(os.path.dirname(__file__), 'opnsense')
            print(f"Copying files from {package_opnsense_path} to {repo_opnsense_path}")
            
            try: 
                shutil.copytree(package_opnsense_path, repo_opnsense_path)
            except Exception as e:
                print(f"Error executing command: {e}")

    def npm_cmd_callback(value: str):
        if value != "init": # or value != "add":
            raise typer.BadParameter("Can only init at the moment")
        return value

    def npm(self, cmd: Annotated[str, typer.Argument(help="init", callback=npm_cmd_callback)] = None):
        print(f"Running nginx proxy manager {cmd}")

        if cmd == "init":
            absolute_path = os.getcwd()
            repo_path = os.path.join(absolute_path, 'npm')
            package_path = os.path.join(os.path.dirname(__file__), 'npm')
            print(f"Copying files from {package_path} to {repo_path}")
            
            try: 
                shutil.copytree(package_path, repo_path)
            except Exception as e:
                print(f"Error executing command: {e}")
