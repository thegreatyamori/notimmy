def main(_typer):
    def _version_callback(value: str) -> None:
        if value in ["BUY", "SELL"]:
            _typer.echo(f"do something with {value}")
            raise _typer.Exit()

        _typer.echo(f"invalid argument: {value}")
        raise _typer.Exit()

    return _typer.Option(
        "SELL",
        "--trade",
        "-t",
        help="Set type of trade to search (BUY | SELL).",
        callback=_version_callback,
    )
