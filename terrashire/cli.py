# Test
import typer
from .terrashire import Terrashire

app = typer.Typer()
terrashire_instance = Terrashire()

app.command()(terrashire_instance.run)
app.command("help")(terrashire_instance.help)
app.command("init")(terrashire_instance.init)
app.command("opnsense")(terrashire_instance.opnsense)
app.command("npm")(terrashire_instance.npm)

if __name__ == "__main__":
    app()
