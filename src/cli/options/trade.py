trade_types = ["BUY", "SELL"]


def main(typer, default):
    def _version_callback(value: str) -> None:
        if value not in trade_types:
            raise typer.BadParameter(f"Only {', '.join(trade_types)} is allowed")

        return value

    return typer.Option(
        default,
        "--trade",
        "-t",
        help="Set type of trade to search (BUY | SELL).",
        callback=_version_callback,
    )
