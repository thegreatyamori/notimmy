def main(_typer):
    def _country_callback(value: str) -> None:
        if value in ["ecuador"]:
            _typer.echo(f"do something with {value}")
            raise _typer.Exit()

        _typer.echo(f"invalid argument: {value}")
        raise _typer.Exit()

    return _typer.Option(
        "ecuador",
        "--country",
        "-c",
        help="Set country name to search (only supports EC).",
        callback=_country_callback,
    )
