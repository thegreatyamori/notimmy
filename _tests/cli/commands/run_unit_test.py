import src.cli.commands as commands


def test__run_calls_logic_methods__when_is_called(mocker, fake_run_command):
    mocks = fake_run_command
    defaults = mocker.Mock(is_running=False)

    commands.start_bot(defaults)

    mocks.run_fetch_live_offers.assert_called()
    mocks.run_process_live_offers.assert_called()
    mocks.execute_jobs.assert_not_called()
