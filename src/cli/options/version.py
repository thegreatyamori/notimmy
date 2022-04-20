__app_name__ = "notimmy"
__version__ = "1.0.0"


def main(typer):
    def _version_callback(value: bool) -> None:
        if value:
            typer.echo(f"{__app_name__} v{__version__}")
            raise typer.Exit()

    return typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
