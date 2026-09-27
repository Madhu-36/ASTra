import typer
app = typer.Typer()
@app.command()
def start():
    print('Starting vanguard_network')
