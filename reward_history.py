import argparse
import json
import os
import shutil
import sys


from api import reward
from api.pool import Pool


def stake_address_reward():
    """
    Example: python reward_history.py -stake_address stake1uxapcr8ekqu4n0rscja2mt8pd4ukk2xyvqxgjveq4tqh52qy9a30y -epoch_start 237 -epoch_end 298

    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-stake_address", help="specify a stake address to output reward history.", type=str)
    parser.add_argument(
        "-epoch_start", help="epoch start", type=int)
    parser.add_argument(
        "-epoch_end", help="epoch end", type=int)
    parser.add_argument(
        "-delegators", help="to get data for delegators, expects y when enabled.", type=str)

    args = parser.parse_args()
    stake_address = args.stake_address
    if args.epoch_start is None:
        epoch_start = 0
    else:
        epoch_start = args.epoch_start
    if args.epoch_end is None:
        epoch_end = None
    else:
        epoch_end = args.epoch_end

    reward_data_folder = "reward_data"
    if os.path.exists(reward_data_folder):
        shutil.rmtree(reward_data_folder)
    os.mkdir(reward_data_folder)

    if args.delegators == "y":
        pool_obj = Pool()
        delg_stake_addresses = pool_obj.pool_delegators()
        for d in delg_stake_addresses:
            stake_address = ""
            stake_address = d["address"]
            rwd = reward.Rewards(stake_address=stake_address)
            rwd.list_rewards()
            rwd.add_rewards()

            with open(os.path.join(reward_data_folder, stake_address + ".json"), "w") as f:
                json.dump(rwd.rewards_list, f)
        sys.exit(0)

    if args.stake_address:
        rwd = reward.Rewards(stake_address=stake_address,
                             epoch_start=epoch_start, epoch_end=epoch_end)
        rwd.list_rewards()
        rwd.print_rewards()
        rwd.add_rewards()
        print(f"{'-'*100}")
        print(f"Sum of rewards: {rwd.rewards_sum/1000000} ADA", )

        with open(os.path.join(reward_data_folder, stake_address + ".json"), "w") as f:
            json.dump(rwd.rewards_list, f)


if __name__ == '__main__':
    stake_address_reward()
