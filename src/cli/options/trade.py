def main(typer, default):
    def _version_callback(value: str) -> None:
        if value not in ["BUY", "SELL"]:
            raise typer.BadParameter("Only 'BUY', 'SELL' is allowed")

        return value

    return typer.Option(
        default,
        "--trade",
        "-t",
        help="Set type of trade to search (BUY | SELL).",
        callback=_version_callback,
    )
