import os
import shutil
import subprocess

def copy(to_path, from_path):
    try: 
        shutil.copytree(to_path, from_path)
    except Exception as e:
        print(f"Error executing command: {e}")

def run(cmd: str, path: str = os.getcwd()):
    cmd_arr = cmd.split(" ")
    try: 
        process = subprocess.run(cmd_arr, cwd=path, capture_output=True, text=True, check=False)
        print(process.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(f"Stderr: {e.stderr}")
