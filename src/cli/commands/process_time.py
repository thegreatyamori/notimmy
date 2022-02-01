def main(_typer):
    def _process_time_callback(value: int) -> None:
        if value > 0:
            _typer.echo(f"do something with {value}")
            raise _typer.Exit()

        _typer.echo(f"invalid argument: {value}")
        raise _typer.Exit()

    return _typer.Option(
        30,
        "--set-process-time",
        "-pt",
        help=(
            "Establishing the frequency in minutes with which "
            "the Binance API data is processed by the app."
        ),
        callback=_process_time_callback,
    )
