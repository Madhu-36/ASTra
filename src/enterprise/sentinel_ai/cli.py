import typer
app = typer.Typer()
@app.command()
def start():
    print('Starting sentinel_ai')
