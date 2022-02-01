from typer.testing import CliRunner

from src.cli.commands import app

runner = CliRunner()


def test__set_fetch_time_option_value__shows_msg__when_cli_is_invoked():
    result = runner.invoke(app, ["--set-fetch-time", 20])
    assert result.exit_code == 0
    assert result.stdout == "do something with 20\n"


def test__set_fetch_time_wrong_option_value_shows_invalid_arg__when_cli_is_invoked():
    result = runner.invoke(app, ["--set-fetch-time", -1])
    assert result.exit_code == 0
    assert result.stdout == "invalid argument: -1\n"


def test__set_fetch_time_empty_option_value_shows_required_arg__when_cli_is_invoked():
    result = runner.invoke(app, ["--set-fetch-time"])
    assert result.exit_code == 2
    assert "set-fetch-time" in result.stdout
    assert "requires" in result.stdout
    assert "argument" in result.stdout
