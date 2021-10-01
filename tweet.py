import argparse
import datetime
import time

from api.ledger import Ledger
from api.pool import Pool
from calc.calc_simul_perf import SimulPerfCalculation
from twitter.twitter import Tweet


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-test", help="specify y to run a test (this does not post), defaulted no.", type=str, default='n')

    args = parser.parse_args()
    if args.test == "y":
        is_test = True
    else:
        is_test = False

    ledger_obj = Ledger()
    _epoch_latest = ledger_obj.latest_epoch()
    epoch_latest = _epoch_latest["epoch"]
    epoch_start_time = _epoch_latest["start_time"]
    epoch_end_time = _epoch_latest["end_time"]

    unix_time = time.time()
    diff = unix_time - epoch_start_time

    five_hours_in_seconds = 5 * 60 * 60
    # Runs if it is within 5 hours after epoch start
    if five_hours_in_seconds >= diff or is_test:
        print(f"Epoch {epoch_latest} has just started!")
        print(_epoch_latest)
        print(f"Epoch: {epoch_latest}")
        print(f"Epoch start time: {epoch_start_time}")
        print(f"Unix time: {unix_time}")
        print(f"Difference: {diff}")

        # dt_now = datetime.datetime.fromtimestamp(
        #     unix_time, datetime.timezone(datetime.timedelta(hours=9)))

        dt_epoch_start = datetime.datetime.fromtimestamp(
            epoch_start_time, datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%d %H:%M")

        dt_epoch_end = datetime.datetime.fromtimestamp(
            epoch_end_time, datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%d %H:%M")

        print(f"Epoch start: {dt_epoch_start}")
        print(f"Epoch end: {dt_epoch_end}")

        # Get pool's performance and blocks minted one epoch ago
        calc_epoch = epoch_latest - 1
        calc_obj = SimulPerfCalculation(calc_epoch)
        calc_obj.get_epoch_stats()
        calc_epoch = calc_obj.params["epoch"]

        pool_obj = Pool()
        p = pool_obj.pool_historical_data(
            calc_epoch)

        calc_obj.set_pool_params(p["active_stake"], p["blocks"])
        calc_obj.calculate_params()

        # print(f'Pool performance: {calc_obj.params["pool_perf"]}')
        performance_in_prct = round(calc_obj.params["pool_perf"] * 100)
        # print(f'Blocks minted: {p["blocks"]}')
        active_stake_in_ada_m = round(
            int(p["active_stake"]) / 1000000 / 1000000, 3)
        # print(f'Active stake: {p["active_stake"]}')

        text = """
プールのご報告
いつも応援ありがとうございます！

Epoch {} の成績
- Blocks minted: {}
- Active stake: {} M
- Pool performance: {} %

Epoch {} もよろしくお願いします！
- Start: {} JST (UTC+9)
- End  : {} JST (UTC+9)

#Cardano #Blockfrost
        """.format(calc_epoch, p["blocks"], active_stake_in_ada_m, performance_in_prct, epoch_latest, dt_epoch_start, dt_epoch_end)
        twitter_obj = Tweet()
        if is_test:
            resp = twitter_obj.test_post(text)
        else:
            resp = twitter_obj.post(text)

        print("Tweet result:")
        print(f"Resp: {resp}")


if __name__ == "__main__":
    main()
