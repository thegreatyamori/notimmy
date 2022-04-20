import typing

import typer

from .commands import start_bot
from .defaults import Defaults
from .options import (
    country_option,
    set__fetch_time_option,
    set__process_time_option,
    trade_option,
    version_option,
)

app = typer.Typer()


@app.command()
def run():
    start_bot(defaults=Defaults)
    typer.echo("Running bot...")


@app.command(name="test-run")
def test_run():
    typer.echo("Fake run command only for tests purposes")


@app.callback()
def main(
        _version: typing.Optional[bool] = version_option(typer),
        _trade: typing.Optional[str] = trade_option(
            typer, default=Defaults.trade
        ),
        _country: typing.Optional[str] = country_option(
            typer, default=Defaults.country
        ),
        _set_fetch_time: typing.Optional[int] = set__fetch_time_option(
            typer, default=Defaults.fetch_time
        ),
        _set_process_time: typing.Optional[int] = set__process_time_option(
            typer, default=Defaults.process_time
        ),
) -> None:
    Defaults.trade = _trade
    Defaults.country = _country
    Defaults.fetch_time = _set_fetch_time
    Defaults.process_time = _set_process_time
    return
