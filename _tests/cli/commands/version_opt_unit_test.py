from typer.testing import CliRunner

from src.cli.commands import app
from src.cli.commands.version import __app_name__, __version__

runner = CliRunner()


def test__version_option__when_cli_is_invoked():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout
