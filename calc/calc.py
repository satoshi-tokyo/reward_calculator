from db.database import Database
from api.ledger import Ledger

EPOCH_BLOCKS = 21600
TM = 45000000000000000


class RewardCalculation(object):
    def __init__(self, epoch):
        self.epoch = epoch
        self.params = {}
        self.db_obj = Database()

    def check_epoch(self):
        data_count = self.db_obj.select_if_epoch_exits(
            self.db_obj.network_supply_table, self.epoch)
        return int(data_count)

    def get_epoch_stats(self):
        ledger_obj = Ledger(self.epoch)
        _params = ledger_obj.epoch_stats()
        self.params["epoch"] = self.epoch
        self.params["total_active_stake"] = int(_params["active_stake"])
        self.params["total_fees"] = int(_params["fees"])
        self.params["block_count"] = int(_params["block_count"])
        self.params["total_blocks"] = EPOCH_BLOCKS

    def get_protocol_params(self):
        ledger_obj = Ledger(self.epoch)
        _params = ledger_obj.parameters()
        # print(_params)
        self.params["max_supply"] = TM
        self.params["rho"] = _params["rho"]
        self.params["tau"] = _params["tau"]
        self.params["a0"] = _params["a0"]
        self.params["k"] = _params["n_opt"]
        self.params["z0"] = 1 / _params["n_opt"]

    def get_total_supply(self):
        db_obj = Database()
        result = db_obj.select_from_network_supply_table(self.epoch)
        self.params["total_supply"] = result[2]  # Total amount
        db_obj.close_db()

    def get_pool_params(self):
        out = self.db_obj.select_from_pool_table(self.epoch)
        # epoch, live_stake, active_stake, declared_pledge, live_pledge, margin_cost, fixed_cost
        self.params["pool_active_stake"] = int(out[2])
        self.params["pool_live_stake"] = int(out[1])
        self.params["declared_pledge"] = int(out[3])
        self.params["live_pledge"] = int(out[4])
        self.params["margin_cost"] = float(out[5])
        self.params["fixed_cost"] = int(out[6])

    def get_pool_blocks_minted(self):
        ledger_obj = Ledger(self.epoch)
        block_count = ledger_obj.pool_blocks_minted_per_epoch()
        self.params["block_minted"] = block_count

    def calculate_params(self):
        # self.params["Re"] = self.params["total_fees"] + self.params["rho"] * \
        #     (self.params["max_supply"] - self.params["total_supply"])

        self.params["Re"] = self.params["rho"] * \
            (self.params["max_supply"] - self.params["total_supply"])

        self.params["total_rewards(R)"] = self.params["Re"] * \
            (1 - self.params["tau"])

        self.params["sigma_prime"] = self.params["pool_active_stake"] / \
            self.params["total_supply"]

        self.params["sigma_a"] = self.params["pool_active_stake"] / \
            self.params["total_active_stake"]

        self.params["s_prime"] = self.params["live_pledge"] / \
            self.params["total_supply"]

        self.params["f_s_sigma"] = (self.params["total_rewards(R)"] / (1 + self.params["a0"])) * (self.params["sigma_prime"] + (self.params["s_prime"] * self.params["a0"]) * (
            self.params["sigma_prime"] - (self.params["s_prime"] * ((self.params["z0"] - self.params["sigma_prime"]) / self.params["z0"]))) / self.params["z0"])

        self.params["beta"] = self.params["block_minted"] / \
            self.params["total_blocks"]

        self.params["pool_perf"] = self.params["beta"] / self.params["sigma_a"]

        self.params["pool_reward"] = self.params["f_s_sigma"] * \
            self.params["pool_perf"]

        self.params["pool_fee"] = self.params["fixed_cost"] + \
            self.params["pool_reward"] * self.params["margin_cost"]

        self.params["delegators_reward"] = self.params["pool_reward"] - \
            self.params["pool_fee"]

    def calculate_delegators_reward(self, stake):
        """
        Returns delegator's reward from specified epoch.
        """
        reward = self.params["delegators_reward"] * \
            stake / self.params["pool_active_stake"]
        return reward
