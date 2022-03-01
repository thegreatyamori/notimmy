def main(typer, default):
    def _fetch_time_callback(value: int) -> None:
        if value < 1:
            raise typer.BadParameter("Only positive values are allowed")

        return value

    return typer.Option(
        default,
        "--set-fetch-time",
        "-ft",
        help=(
            "Establish the frequency in minutes with which "
            "the Binance API data is captured."
        ),
        callback=_fetch_time_callback,
    )
