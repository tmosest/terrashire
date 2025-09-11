# Test
import typer
from .terrashire import Terrashire

app = typer.Typer()
terrashire_instance = Terrashire()

app.command()(terrashire_instance.run)
app.command("help")(terrashire_instance.help)
app.command("init")(terrashire_instance.init)
app.command("list_network")(terrashire_instance.list_network)
app.command("detect_new_devices")(terrashire_instance.detect_new_devices)
# Modules TODO dynamic
app.command("gitea")(terrashire_instance.gitea)
app.command("opnsense")(terrashire_instance.opnsense)
app.command("npm")(terrashire_instance.npm)
app.command("pihole")(terrashire_instance.pihole)
app.command("proxmox")(terrashire_instance.proxmox)
app.command("woodpecker")(terrashire_instance.woodpecker)

if __name__ == "__main__":
    app()
