def main(typer, default):
    def _process_time_callback(value: int) -> None:
        if value < 1:
            raise typer.BadParameter("Only positive values are allowed")

        return value

    return typer.Option(
        default,
        "--set-process-time",
        "-pt",
        help=(
            "Establish the frequency in minutes with which "
            "the Binance API data is processed by the app."
        ),
        callback=_process_time_callback,
    )
