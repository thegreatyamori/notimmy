from typer.testing import CliRunner

from main import cli

runner = CliRunner()


def test__country_option__returns_the_value__when_cli_is_invoked():
    result = runner.invoke(cli, ["--country", "ecuador", "test-run"])

    assert result.exit_code == 0


def test__country_wrong_option_value_shows_an_error__when_cli_is_invoked():
    expected_message = "Only ecuador is allowed"

    result = runner.invoke(cli, ["--country", "test", "test-run"])

    assert result.exit_code == 2
    assert expected_message in result.stdout


def test__country_empty_option_value_shows_required_arg__when_cli_is_invoked():
    result = runner.invoke(cli, ["--country"])

    assert result.exit_code == 2
    assert "country" in result.stdout
    assert "requires" in result.stdout
    assert "argument" in result.stdout
