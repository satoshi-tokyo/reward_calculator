import argparse
import csv
import os


from api.pool import Pool


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-pool", help="retrieves data and outputs", type=str)

    args = parser.parse_args()

    if args.pool == "all":
        simul_folder = "csv"
        if not os.path.exists(simul_folder):
            os.mkdir(simul_folder)
        pool_obj = Pool()
        pool_obj.pool_list_all()
        with open(os.path.join(simul_folder, 'pool_info_list.csv'), 'w') as f:
            writer = csv.writer(f)
            data = ["pool_id",
                    "hex",
                    "vrf_key",
                    "blocks_minted",
                    "live_stake",
                    "live_size",
                    "live_saturation",
                    "live_delegators",
                    "active_stake",
                    "active_size",
                    "declared_pledge",
                    "live_pledge",
                    "margin_cost",
                    "fixed_cost",
                    "reward_account",
                    "owners",
                    "registration",
                    "retirement"
                    ]
            writer.writerow(data)
            count = 1
            for pool_id in pool_obj.pool_list:
                p = pool_obj.specific_pool(pool_id)

                if "status_code" in p.keys():
                    if p["status_code"] == 404:
                        print(
                            "Pool information not found. Looks like the loop has reached the last page.")
                        break

                data = [p["pool_id"],
                        p["hex"],
                        p["vrf_key"],
                        p["blocks_minted"],
                        p["live_stake"],
                        p["live_size"],
                        p["live_saturation"],
                        p["live_delegators"],
                        p["active_stake"],
                        p["active_size"],
                        p["declared_pledge"],
                        p["live_pledge"],
                        p["margin_cost"],
                        p["fixed_cost"],
                        p["reward_account"],
                        p["owners"],
                        p["registration"],
                        p["retirement"]
                        ]
                writer.writerow(data)
                count += 1


if __name__ == '__main__':
    main()
