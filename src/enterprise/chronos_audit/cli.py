import typer
app = typer.Typer()
@app.command()
def start():
    print('Starting chronos_audit')
