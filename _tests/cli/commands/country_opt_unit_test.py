from typer.testing import CliRunner

from src.cli.commands import app

runner = CliRunner()


def test__country_option_value__shows_msg__when_cli_is_invoked():
    result = runner.invoke(app, ["--country", "ecuador"])
    assert result.exit_code == 0
    assert result.stdout == "do something with ecuador\n"


def test__country_wrong_option_value_shows_invalid_arg__when_cli_is_invoked():
    result = runner.invoke(app, ["--country", "test"])
    assert result.exit_code == 0
    assert result.stdout == "invalid argument: test\n"


def test__country_empty_option_value_shows_required_arg__when_cli_is_invoked():
    result = runner.invoke(app, ["--country"])
    assert result.exit_code == 2
    assert "country" in result.stdout
    assert "requires" in result.stdout
    assert "argument" in result.stdout
