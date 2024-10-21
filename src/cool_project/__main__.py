import typer

from cool_project.calculus import sum_small_numbers

app = typer.Typer()


@app.command()
def hello(name: str):
    """Say hello to the provided name."""
    typer.echo(f"Hello {name} !")


@app.command()
def do_sum(a: int, b: int):
    """Sum two small numbers."""
    try:
        result = sum_small_numbers(a, b)
        typer.echo(f"Result: {result}")
    except ValueError as e:
        raise typer.BadParameter(str(e))


@app.command()
def weather(latitude: float, longitude: float):
    """Display the weather for a specific geolocation."""
    typer.echo(f"Getting weather for {latitude}, {longitude}...")


if __name__ == "__main__":
    app()  # pragma: no cover
