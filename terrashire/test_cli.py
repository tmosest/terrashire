import os
import unittest
from typer.testing import CliRunner


from .cli import app  # Import your Typer app

runner = CliRunner()

def test_help():
    result = runner.invoke(app, ["help"])
    assert result.exit_code == 0
    assert "Terrashire" in result.stdout

def test_init():
    path =  os.path.join(os.path.expanduser("~"), 'terrashire-cli-test-units')
    result = runner.invoke(app, ["init", path])
    assert result.exit_code == 0
    assert "Initializing homelab iac" in result.stdout
    assert "Copying files from" in result.stdout
    assert "Reinitialized existing Git repository in" in result.stdout

'''
def test_list_network():
    result = runner.invoke(app, ["list_network"])
    assert result.exit_code == 0
    assert "Initializing homelab iac" in result.stdout
    assert "Copying files from" in result.stdout
    assert "Reinitialized existing Git repository in" in result.stdout
'''

def test_gitea_init():
    path =  os.path.join(os.path.expanduser("~"), 'terrashire-cli-test-units')
    print(f"{path}")
    runner.invoke(app, ["init", path])

    result = runner.invoke(app, ["init", path])
    assert result.exit_code == 0
    
    os.chdir(path)
    result = runner.invoke(app, ["gitea", "init"])

    assert result.exit_code == 0
    assert "/gitea" in result.stdout

def test_mods_init():
    path =  os.path.join(os.path.expanduser("~"), 'terrashire-cli-test-units')
    print(f"{path}")
    runner.invoke(app, ["init", path])

    result = runner.invoke(app, ["init", path])
    assert result.exit_code == 0

    mods = ["opnsense", "npm", "gitea", "pihole", "proxmox", "woodpecker"]
    
    for mod in mods:
        os.chdir(path)
        result = runner.invoke(app, [mod, "init"])
        
        assert result.exit_code == 0
        assert f"/{mod}" in result.stdout
