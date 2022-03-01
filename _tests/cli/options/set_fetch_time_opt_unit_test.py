from typer.testing import CliRunner

from main import cli

runner = CliRunner()


def test__set_fetch_time_option__returns_the_value__when_cli_is_invoked():
    result = runner.invoke(cli, ["--set-fetch-time", 20, "fake-run"])

    assert result.exit_code == 0


def test__set_fetch_time_wrong_option_value_shows__an_error__when_cli_is_invoked():
    expected_message = "Only positive values are allowed"

    result = runner.invoke(cli, ["--set-fetch-time", -1, "fake-run"])

    assert result.exit_code == 2
    assert expected_message in result.stdout


def test__set_fetch_time_empty_option_value_shows_required_arg__when_cli_is_invoked():
    result = runner.invoke(cli, ["--set-fetch-time"])

    assert result.exit_code == 2
    assert "set-fetch-time" in result.stdout
    assert "requires" in result.stdout
    assert "argument" in result.stdout
