def main(typer, default):
    def _country_callback(value: str) -> None:
        if value not in ["ecuador"]:
            raise typer.BadParameter("Only 'ecuador' is allowed")

        return value

    return typer.Option(
        default,
        "--country",
        "-c",
        help="Set country name to search (only supports EC).",
        callback=_country_callback,
    )
