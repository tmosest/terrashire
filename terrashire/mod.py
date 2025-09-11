import abc
import os
import typer

from .cmd_util import copy
from .config import Config

class Mod(abc.ABC):

    def init_mod(self):
        absolute_path = os.getcwd()
        repo_path = os.path.join(absolute_path, self.get_mod())
        package_path = os.path.join(os.path.dirname(__file__), self.get_mod())
        print(f"Copying files from {package_path} to {repo_path}")
            
        try: 
            copy(package_path, repo_path)
        except Exception as e:
            print(f"Error executing command: {e}")

        self.init_mod_secrets_prompts()

    def init_mod_secrets_prompts(self):
        absolute_path = os.getcwd()
        repo_path = os.path.join(absolute_path, self.get_mod())
        terraform_vars_path = os.path.join(repo_path, 'terraform.tfvars')

        # Skip mods without tfvars files for now.
        # TODO set env variables for docker and other stuff.
        if os.path.exists(terraform_vars_path) == False:
            return
        
        config = Config.loadConfig()

        contents = []

        with open(terraform_vars_path, "r") as file:
            contents = file.readlines()

        results = []

        config.data[self.get_mod()] = {}

        for content in contents:
            question = content.split("=")[0].strip()
            ans = typer.prompt(question)
            results.append(f"{question} = \"{ans}\"")
            config.data[self.get_mod()][question] = ans

        with open(terraform_vars_path, "w") as file:
            for item in results:
                file.write(str(item) + "\n")

        config.saveConfig()

    
    @abc.abstractmethod
    def init(self):
        pass

    def get_mod(self):
        return self.mod
