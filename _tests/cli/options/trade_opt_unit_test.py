import pytest
from typer.testing import CliRunner

from main import cli

runner = CliRunner()


@pytest.mark.parametrize("value", ['BUY', 'SELL'])
def test__trade_option__returns_the_value__when_cli_is_invoked(value):
    result = runner.invoke(cli, ["--trade", value, "test-run"])

    assert result.exit_code == 0


def test__trade_wrong_option_value_shows_an_error__when_cli_is_invoked():
    expected_message = "Only BUY, SELL is allowed"

    result = runner.invoke(cli, ["--trade", "test", "test-run"])

    assert result.exit_code == 2
    assert expected_message in result.stdout


def test__trade_empty_option_value_shows_required_arg__when_cli_is_invoked():
    result = runner.invoke(cli, ["--trade"])

    assert result.exit_code == 2
    assert "trade" in result.stdout
    assert "requires" in result.stdout
    assert "argument" in result.stdout
