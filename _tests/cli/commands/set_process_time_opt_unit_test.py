from typer.testing import CliRunner

from src.cli.commands import app

runner = CliRunner()


def test__set_process_time_option_value__shows_msg__when_cli_is_invoked():
    result = runner.invoke(app, ["--set-process-time", 30])
    assert result.exit_code == 0
    assert result.stdout == "do something with 30\n"


def test__set_process_time_wrong_option_value_shows_invalid_arg__when_cli_is_invoked():
    result = runner.invoke(app, ["--set-process-time", -5])
    assert result.exit_code == 0
    assert result.stdout == "invalid argument: -5\n"


def test__set_process_time_empty_option_value_shows_required_arg__when_cli_is_invoked():
    result = runner.invoke(app, ["--set-process-time"])
    assert result.exit_code == 2
    assert "set-process-time" in result.stdout
    assert "requires" in result.stdout
    assert "argument" in result.stdout
