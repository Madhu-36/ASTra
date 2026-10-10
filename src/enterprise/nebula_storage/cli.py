import typer
app = typer.Typer()
@app.command()
def trigger():
    print('Triggering nebula_storage')
