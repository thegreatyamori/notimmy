def main(_typer):
    def _fetch_time_callback(value: int) -> None:
        if value > 0:
            _typer.echo(f"do something with {value}")
            raise _typer.Exit()

        _typer.echo(f"invalid argument: {value}")
        raise _typer.Exit()

    return _typer.Option(
        10,
        "--set-fetch-time",
        "-ft",
        help=(
            "Establishing the frequency in minutes with which "
            "the Binance API data is captured."
        ),
        callback=_fetch_time_callback,
    )
