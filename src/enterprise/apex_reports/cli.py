import typer
app = typer.Typer()
@app.command()
def start():
    print('Starting apex_reports')
