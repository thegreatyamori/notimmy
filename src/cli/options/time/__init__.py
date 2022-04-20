from .time import main


def set__process_time_option(typer, default):
    kwargs = {
        'flag': '--set-process-time',
        'flag_shortcut': '-pt',
        'help': (
            "Establish the frequency in minutes with which "
            "the Binance API data is processed by the app."
        )
    }
    return main(typer, default, **kwargs)


def set__fetch_time_option(typer, default):
    kwargs = {
        'flag': '--set-fetch-time',
        'flag_shortcut': '-ft',
        'help': (
            "Establish the frequency in minutes with which "
            "the Binance API data is captured."
        )
    }
    return main(typer, default, **kwargs)
