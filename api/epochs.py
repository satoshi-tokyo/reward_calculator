import datetime

from api import ledger


def epoch_stake_timing():
    """ This module retrieves epoch start and end date/time, as well as timings its timing for the stake to be effective.
        Returns:
            epochs(list): list of dictionaries of epoch information.
    """

    ledger_obj = ledger.Ledger()
    _epoch_latest = ledger_obj.latest_epoch()
    epoch_latest = _epoch_latest["epoch"]
    epoch_start_time = _epoch_latest["start_time"]
    epoch_end_time = _epoch_latest["end_time"]

    # Get a list of epoch start and end dates, and delegation epochs.
    epochs = []
    for e in range(epoch_latest - 9, epoch_latest + 1):
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


if __name__ == "__main__":
    epoch_stake_timing()
