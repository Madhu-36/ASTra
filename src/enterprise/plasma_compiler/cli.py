import typer
app = typer.Typer()
@app.command()
def trigger():
    print('Triggering plasma_compiler')
