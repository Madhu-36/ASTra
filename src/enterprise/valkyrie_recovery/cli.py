import typer
app = typer.Typer()
@app.command()
def trigger():
    print('Triggering valkyrie_recovery')
