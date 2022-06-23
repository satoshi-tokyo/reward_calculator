import argparse
import datetime
import time

from api.ledger import Ledger
from api.pool import Pool
from calc.calc_simul_perf import SimulPerfCalculation
from twitter.twitter import Tweet
from twitter import text as txt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-test", help="specify y to run a test (disables posting a tweet), defaulted no.", type=str, default='n')
    parser.add_argument(
        "-post", help="specify y to post pool performance, defaulted no.", type=str, default='n')

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

    # Set current time or epoch start time in which case postting message will run.
    if args.post == "y":
        unix_time = epoch_start_time
    else:
        unix_time = time.time()

    print(f"Unix time: {unix_time}")
    print(f"Epoch start time: {epoch_start_time}")
    print(f"Epoch end time: {epoch_end_time}")
    one_day_in_seconds = 24 * 60 * 60
    first_day_end = epoch_start_time + one_day_in_seconds
    second_day_end = epoch_start_time + 2 * one_day_in_seconds
    third_day_end = epoch_start_time + 3 * one_day_in_seconds
    fourth_day_end = epoch_start_time + 4 * one_day_in_seconds
    fifth_day_end = epoch_start_time + 5 * one_day_in_seconds

    twitter_obj = Tweet()
    if unix_time >= fourth_day_end and unix_time < fifth_day_end:
        print("DAY 5")
        text = txt.day5()
    elif unix_time >= third_day_end and unix_time < fourth_day_end:
        print("DAY 4")
        text = txt.day4()
    elif unix_time >= second_day_end and unix_time < third_day_end:
        print("DAY 3")
        text = txt.day3()
    elif unix_time >= first_day_end and unix_time < second_day_end:
        print("DAY 2")
        text = txt.day2()
    elif unix_time >= epoch_start_time and unix_time < first_day_end:
        print("DAY 1")
        print(f"Epoch {epoch_latest} has just started!")
        print(_epoch_latest)
        print(f"Epoch: {epoch_latest}")
        print(f"Epoch start time: {epoch_start_time}")
        print(f"Unix time: {unix_time}")
        # print(f"Difference: {diff}")

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

        if performance_in_prct == 0:
            text = """
プールのご報告
申し訳ありません。
今回ブロックの割り当てはございませんでした。

Epoch {} の成績
- Blocks minted: {}
- Active stake: {} M

Epoch {} もサーバ運用はしっかりと実施いたします。
- Start: {} JST (UTC+9)
- End  : {} JST (UTC+9)

#Cardano
        """.format(calc_epoch, p["blocks"], active_stake_in_ada_m, epoch_latest, dt_epoch_start, dt_epoch_end)

        elif performance_in_prct < 50:
            text = """
プールのご報告
今回の割り当ては少ない結果でした。
申し訳ありません。

Epoch {} の成績
- Blocks minted: {}
- Active stake: {} M
- Pool performance: {} %

Epoch {} も尽力します！
- Start: {} JST (UTC+9)
- End  : {} JST (UTC+9)

#Cardano
        """.format(calc_epoch, p["blocks"], active_stake_in_ada_m, performance_in_prct, epoch_latest, dt_epoch_start, dt_epoch_end)

        elif performance_in_prct >= 50 and performance_in_prct < 100:
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

#Cardano
        """.format(calc_epoch, p["blocks"], active_stake_in_ada_m, performance_in_prct, epoch_latest, dt_epoch_start, dt_epoch_end)

        elif performance_in_prct >= 100:
            text = """
プールのご報告
いつもありがとうございます！
お陰様で良い成績でした！

Epoch {} の成績
- Blocks minted: {}
- Active stake: {} M
- Pool performance: {} %

Epoch {} も気を抜かず精進します。
- Start: {} JST (UTC+9)
- End  : {} JST (UTC+9)

#Cardano
        """.format(calc_epoch, p["blocks"], active_stake_in_ada_m, performance_in_prct, epoch_latest, dt_epoch_start, dt_epoch_end)

    if is_test:
        resp = twitter_obj.test_post(text)
    else:
        resp = twitter_obj.post(text)
    print("Tweet result:")
    print(f"Resp: {resp}")


if __name__ == "__main__":
    main()
