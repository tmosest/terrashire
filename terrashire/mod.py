import abc
import os

from .cmd_util import copy

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
    
    @abc.abstractmethod
    def init(self):
        pass

    def get_mod(self):
        return self.mod
