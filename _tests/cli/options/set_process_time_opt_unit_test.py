from typer.testing import CliRunner

from main import cli

runner = CliRunner()


def test__set_process_time_option__returns_the_value__when_cli_is_invoked():
    result = runner.invoke(cli, ["--set-process-time", 30, "test-run"])

    assert result.exit_code == 0


def test__set_process_time_wrong_option_value_shows_invalid_arg__when_cli_is_invoked():
    expected_message = "Only positive values are allowed"

    result = runner.invoke(cli, ["--set-process-time", -5, "test-run"])

    assert result.exit_code == 2
    assert expected_message in result.stdout


def test__set_process_time_empty_option_value_shows_required_arg__when_cli_is_invoked():
    result = runner.invoke(cli, ["--set-process-time"])

    assert result.exit_code == 2
    assert "set-process-time" in result.stdout
    assert "requires" in result.stdout
    assert "argument" in result.stdout
