from typer.testing import CliRunner

from src.cli.commands import app

runner = CliRunner()


def test__trade_buy_option_value__shows_msg__when_cli_is_invoked():
    result = runner.invoke(app, ["--trade", "BUY"])
    assert result.exit_code == 0
    assert result.stdout == "do something with BUY\n"


def test__trade_sell_option_value__shows_msg__when_cli_is_invoked():
    result = runner.invoke(app, ["--trade", "SELL"])
    assert result.exit_code == 0
    assert result.stdout == "do something with SELL\n"


def test__trade_wrong_option_value_shows_invalid_arg__when_cli_is_invoked():
    result = runner.invoke(app, ["--trade", "test"])
    assert result.exit_code == 0
    assert result.stdout == "invalid argument: test\n"


def test__trade_empty_option_value_shows_required_arg__when_cli_is_invoked():
    result = runner.invoke(app, ["--trade"])
    assert result.exit_code == 2
    assert "trade" in result.stdout
    assert "requires" in result.stdout
    assert "argument" in result.stdout
