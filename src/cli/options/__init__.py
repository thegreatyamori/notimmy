import typing

import typer

from ..defaults import Defaults
from ..commands import run as run_service
from .trade import main as __trade_option
from .version import main as __version_option
from .country import main as __country_option
from .fetch_time import main as __set__fetch_time_option
from .process_time import main as __set__process_time_option

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(7)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    DB_READ_ERROR: "database read error",
    DB_WRITE_ERROR: "database write error",
    ID_ERROR: "app id error",
}


app = typer.Typer()


@app.command()
def run():
    run_service(defaults=Defaults)


@app.command(name="fake-run")
def fake_run():
    typer.echo("Fake run command only for tests purposes")


@app.callback()
def main(
    _version: typing.Optional[bool] = __version_option(typer),
    _trade: typing.Optional[str] = __trade_option(typer, default=Defaults.trade),
    # _country: typing.Optional[str] = __country_option(typer),
    # _set_fetch_time: typing.Optional[int] = __set__fetch_time_option(typer),
    # _set_process_time: typing.Optional[int] = __set__process_time_option(typer),
) -> None:
    Defaults.trade = _trade
    return
