import datetime

from api import ledger


def epoch_stake_timing(epoch_count):
    """ This module retrieves epoch start and end date/time, as well as timings its timing for the stake to be effective.
        Args:
            epoch_numbers(int): number of epochs, to get data of, starting from the current epoch
        Returns:
            epochs(list): list of dictionaries of epoch information.
    """
    epoch_count = epoch_count - 1

    ledger_obj = ledger.Ledger()
    _epoch_latest = ledger_obj.latest_epoch()
    epoch_latest = _epoch_latest["epoch"]
    epoch_start_time = _epoch_latest["start_time"]
    epoch_end_time = _epoch_latest["end_time"]

    # Get a list of epoch start and end dates, and delegation epochs.
    epochs = []
    for e in range(epoch_latest - epoch_count, epoch_latest + 1):
        epoch_info = {}
        ledger_obj = ledger.Ledger(e)
        _e = ledger_obj.epoch_stats()
        epoch = _e["epoch"]
        epoch_start_time = _e["start_time"]
        epoch_end_time = _e["end_time"]

        dt_epoch_start = datetime.datetime.fromtimestamp(
            epoch_start_time, datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%d %H:%M")

        dt_epoch_end = datetime.datetime.fromtimestamp(
            epoch_end_time, datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%d %H:%M")

        ledger_obj_deleg = ledger.Ledger(e - 4)
        _e_deleg = ledger_obj_deleg.epoch_stats()
        epoch_deleg = _e_deleg["epoch"]
        epoch_deleg_start_time = _e_deleg["start_time"]
        epoch_deleg_end_time = _e_deleg["end_time"]

        dt_epoch_delg_start = datetime.datetime.fromtimestamp(
            epoch_deleg_start_time, datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%d %H:%M")

        dt_epoch_delg_end = datetime.datetime.fromtimestamp(
            epoch_deleg_end_time, datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%d %H:%M")

        epoch_info = {
            "epoch": epoch,
            "start_time": dt_epoch_start,
            "end_time": dt_epoch_end,
            "epoch_deleg": epoch_deleg,
            "start_time_deleg": dt_epoch_delg_start,
            "end_time_deleg": dt_epoch_delg_end,
        }
        epochs.append(epoch_info)

    return epochs


def epoch_stake_timing_in_future(epoch_away_in_count):
    """ This module returns epoch start and end date/time. 
        Epoch is specified how many epochs are away from the current one.

        Args:
            future_epoch_count(int): number of epochs, away from the current one.
        Returns:
            epoch(dict): a dictionary of epoch information.
    """
    ledger_obj = ledger.Ledger()
    _epoch_latest = ledger_obj.latest_epoch()
    epoch_latest = _epoch_latest["epoch"]
    epoch_start_time = _epoch_latest["start_time"]
    epoch_end_time = _epoch_latest["end_time"]

    epoch_info = {}

    time_away = epoch_away_in_count * 5 * 24 * 60 * 60

    ledger_obj = ledger.Ledger(epoch_latest)
    _e = ledger_obj.epoch_stats()
    epoch = _e["epoch"] + epoch_away_in_count
    epoch_start_time = _e["start_time"] + time_away
    epoch_end_time = _e["end_time"] + time_away

    dt_epoch_start = datetime.datetime.fromtimestamp(
        epoch_start_time, datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%d %H:%M")

    dt_epoch_end = datetime.datetime.fromtimestamp(
        epoch_end_time, datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%d %H:%M")

    ledger_obj_deleg = ledger.Ledger(epoch - 4)
    _e_deleg = ledger_obj_deleg.epoch_stats()
    epoch_deleg = _e_deleg["epoch"]
    epoch_deleg_start_time = _e_deleg["start_time"]
    epoch_deleg_end_time = _e_deleg["end_time"]

    dt_epoch_delg_start = datetime.datetime.fromtimestamp(
        epoch_deleg_start_time, datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%d %H:%M")

    dt_epoch_delg_end = datetime.datetime.fromtimestamp(
        epoch_deleg_end_time, datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%d %H:%M")

    epoch_info = {
        "epoch": epoch,
        "start_time": dt_epoch_start,
        "end_time": dt_epoch_end,
        "epoch_deleg": epoch_deleg,
        "start_time_deleg": dt_epoch_delg_start,
        "end_time_deleg": dt_epoch_delg_end,
    }
    return epoch_info


if __name__ == "__main__":
    epoch_stake_timing()
