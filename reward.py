import argparse
import csv
import json
import os
import sys

from calc.calc import RewardCalculation
from calc.calc_simul_active_stake import SimulRewardCalculation
from calc.calc_simul_perf import SimulPerfCalculation
from db.database import Database
from api.ledger import Ledger
from api.pool import Pool


def latest_data():
    """Latest data is retrieved and stored into database
    """
    ledger_obj = Ledger()
    _epoch_latest = ledger_obj.latest_epoch()
    epoch_latest = _epoch_latest["epoch"]

    # Get network data
    network_latest = ledger_obj.network()

    # Get pool data
    pool_obj = Pool()
    pool_latest = pool_obj.specific_pool()  # Insert into DB every epoch

    db_obj = Database()

    # Create database if not exists
    db_obj.createdb()

    # Insert/update data of supply
    data_count = db_obj.select_if_epoch_exits(
        db_obj.network_supply_table, epoch_latest)

    if data_count == 0:
        db_obj.insert_network_supply(epoch_latest, network_latest)
    elif data_count == 1:
        db_obj.update_network_supply(epoch_latest, network_latest)
    else:
        pass

    # Insert/update data of stake
    data_count = db_obj.select_if_epoch_exits(
        db_obj.network_stake_table, epoch_latest)

    if data_count == 0:
        db_obj.insert_network_stake(epoch_latest, network_latest)
    elif data_count == 1:
        db_obj.update_network_stake(epoch_latest, network_latest)
    else:
        pass

    # Insert/update data of pool
    data_count = db_obj.select_if_epoch_exits(
        db_obj.pool_table, epoch_latest)
    if data_count == 0:
        db_obj.insert_pool(epoch_latest, pool_latest)
    elif data_count == 1:
        db_obj.update_pool(epoch_latest, pool_latest)
    else:
        pass

    # For debug useage
    db_obj._select()

    db_obj.close_db()


def main():
    _current_epoch = Ledger().latest_epoch()
    cur_epoch = int(_current_epoch["epoch"])

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-epoch", help="specify epoch you want to know reward of. Default is current epoch.", type=int, default=cur_epoch)
    parser.add_argument(
        "-stake", help="specify stake amount you are delegating in ADA.", type=float)
    parser.add_argument(
        "-simul", help="to simulate with active_stake, pledge, etc..", type=str)
    # TODO to re-write output data
    parser.add_argument(
        "-db", help="retrieves data and outputs", action="store_true")

    args = parser.parse_args()

    is_current_epoch = False
    if args.epoch == cur_epoch:
        is_current_epoch = True

    # Take data from 2 epochs ago, and calculate reward of it.
    calc_epoch = args.epoch - 2

    if calc_epoch == cur_epoch:
        print("Cannot calculate reward using current epoch's data as it is not finalized, e.g., blocks.")
        sys.exit(1)

    data_folder = "json"
    if args.db:
        # Prepare database and historical data
        latest_data()
        if not os.path.exists(data_folder):
            os.mkdir(data_folder)

    if args.simul == "active_stake":
        if args.stake:
            print("Simulation not permitted to specify stake.")
            sys.exit(1)
        simul_folder = "csv"
        if not os.path.exists(simul_folder):
            os.mkdir(simul_folder)

        calc_obj = SimulRewardCalculation(calc_epoch)
        data_exists = calc_obj.check_epoch()
        if not data_exists:
            print(f"No data from epoch {calc_epoch} exists in database.")
            sys.exit(1)
        calc_obj.get_epoch_stats()
        calc_obj.get_protocol_params()
        calc_obj.get_total_supply()
        _100K = 100000 * 1000000
        _1M = 1000000 * 1000000
        _100M = 100000000 * 1000000

        with open(os.path.join(simul_folder, 'simul_pool_active_stake.csv'), 'w') as f:
            writer = csv.writer(f)
            data = ["active_stake_in_ada", "reward"]
            writer.writerow(data)
            for active_stake in range(_1M, _100M, _1M):
                calc_obj.get_pool_params(active_stake)
                # calc_obj.get_pool_blocks_minted()
                calc_obj.calculate_params()
                reward = calc_obj.calculate_delegators_reward(_100K) / 1000000
                # If reward is minus value due to subtraction of fixed fee, set 0 as it is not realistic
                if reward < 0:
                    reward = 0

                print(
                    f"Active Stake:{active_stake}, Reward: {reward}")
                active_stake_in_ada = active_stake / 1000000
                data = [active_stake_in_ada, reward]
                writer.writerow(data)

        sys.exit(0)

    # Process for pool performance vs active stake
    if args.simul == "perf":
        if args.stake:
            print("Simulation not permitted to specify stake.")
            sys.exit(1)
        simul_folder = "csv"
        if not os.path.exists(simul_folder):
            os.mkdir(simul_folder)

        # Takes data from 2 epochs ago.
        # Active stake and total blocks (21600)
        calc_obj = SimulPerfCalculation(calc_epoch)
        calc_obj.get_epoch_stats()
        calc_epoch = calc_obj.params["epoch"]
        total_active_stake = calc_obj.params["total_active_stake"]
        total_blocks = calc_obj.params["total_blocks"]

        pool_obj = Pool()
        pool_obj.pool_list_all()
        with open(os.path.join(simul_folder, 'pool_perf_active_staket.csv'), 'w') as f:
            writer = csv.writer(f)
            data = ["epoch",
                    "total_active_stake",
                    "total_blocks",
                    "pool_id",
                    "blocks",
                    "active_stake",
                    "active_size",
                    "delegators_count",
                    "rewards",
                    "fees",
                    "pool_perf"
                    ]
            writer.writerow(data)

            for pool_id in pool_obj.pool_list:
                p = pool_obj.pool_historical_data(
                    calc_epoch, ext_pool_id=pool_id)
                if "status_code" in p.keys():
                    if p["status_code"] == 404:
                        print(
                            "Pool information not found. Looks like the loop has reached the last page.")
                        break
                if "status" in p.keys():
                    if p["status"] == "Epoch data not found":
                        print(p["message"])
                        continue

                calc_obj.set_pool_params(p["active_stake"], p["blocks"])
                calc_obj.calculate_params()
                data = [calc_epoch,
                        total_active_stake,
                        total_blocks,
                        pool_id,
                        p["blocks"],
                        p["active_stake"],
                        p["active_size"],
                        p["delegators_count"],
                        p["rewards"],
                        p["fees"],
                        calc_obj.params["pool_perf"]
                        ]
                print(data)
                writer.writerow(data)

            sys.exit(0)

    calc_obj = RewardCalculation(calc_epoch)
    data_exists = calc_obj.check_epoch()
    if not data_exists:
        print(f"No data from epoch {calc_epoch} exists in database.")
        sys.exit(1)
    # Get necessary parameters
    calc_obj.get_epoch_stats()
    calc_obj.get_protocol_params()
    calc_obj.get_total_supply()
    calc_obj.get_pool_params()
    calc_obj.get_pool_blocks_minted()
    calc_obj.calculate_params()

    # If db is specified, write to json file with params.
    if args.db:
        if is_current_epoch:
            # Write data.json current epoch's reward
            with open(os.path.join(data_folder, 'data.json'), 'w') as f:
                json.dump(calc_obj.params, f)
        else:
            # e{epoch#}.json for historical data of the epoch
            epoch_data_json = "e" + str(calc_obj.params["epoch"]) + ".json"
            with open(os.path.join(data_folder, epoch_data_json), 'w') as f:
                json.dump(calc_obj.params, f)

    # If stake is specified, calculate reward of that stake.
    if args.stake and args.simul is None:
        calc_stake = args.stake * 1000000
        reward = calc_obj.calculate_delegators_reward(calc_stake) / 1000000
        print(f"Reward: {reward} ADA")

    # If no stake is specified, output data.
    if args.stake is None and args.simul is None:
        print(
            f"Output epoch {calc_obj.params['epoch']} pool reward and parameters..")
        print(calc_obj.params)


if __name__ == '__main__':
    main()
