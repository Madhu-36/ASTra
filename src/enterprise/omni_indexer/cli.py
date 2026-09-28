import typer
app = typer.Typer()
@app.command()
def trigger():
    print('Triggering omni_indexer')
