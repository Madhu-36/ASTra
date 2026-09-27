import typer
app = typer.Typer()
@app.command()
def start():
    print('Starting optics_telemetry')
