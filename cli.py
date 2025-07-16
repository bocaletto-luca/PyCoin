# cli.py
import typer
from pycoin.wallet import Wallet
from pycoin.api import app as api_app

cli = typer.Typer()

@cli.command()
def create_wallet(password: str = typer.Option("", help="Encrypt private key")):
    priv, pub = Wallet.generate_keys(password.encode())
    with open("private.pem", "wb") as f: f.write(priv)
    with open("public.pem", "wb")  as f: f.write(pub)
    typer.echo("Wallet created: private.pem & public.pem")

@cli.command()
def run_node(port: int = 8000):
    import uvicorn
    uvicorn.run(api_app, host="0.0.0.0", port=port)

if __name__ == "__main__":
    cli()
