countries = ["ecuador"]


def main(typer, default):
    def _country_callback(value: str) -> None:
        if value not in countries:
            raise typer.BadParameter(f"Only {', '.join(countries)} is allowed")

        return value

    return typer.Option(
        default,
        "--country",
        "-c",
        help="Set country name to search (only supports EC).",
        callback=_country_callback,
    )
