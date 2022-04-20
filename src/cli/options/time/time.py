def main(typer, default, **kwargs):
    def _time_callback(value: int) -> None:
        if value < 1:
            raise typer.BadParameter("Only positive values are allowed")

        return value

    return typer.Option(
        default,
        kwargs['flag'],
        kwargs['flag_shortcut'],
        help=kwargs['help'],
        callback=_time_callback,
    )
