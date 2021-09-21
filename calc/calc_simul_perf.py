# from db.database import Database
from api.ledger import Ledger

EPOCH_BLOCKS = 21600
TM = 45000000000000000


class SimulPerfCalculation(object):
    def __init__(self, epoch):
        self.epoch = epoch
        self.params = {}
        # self.db_obj = Database()

    def get_epoch_stats(self):
        ledger_obj = Ledger(self.epoch)
        _params = ledger_obj.epoch_stats()
        self.params["epoch"] = self.epoch
        self.params["total_active_stake"] = int(_params["active_stake"])
        self.params["total_fees"] = int(_params["fees"])
        self.params["block_count"] = int(_params["block_count"])
        self.params["total_blocks"] = EPOCH_BLOCKS

    def set_pool_params(self, pool_active_stake, block_minted):
        self.params["pool_active_stake"] = int(pool_active_stake)
        self.params["block_minted"] = int(block_minted)

    def calculate_params(self):
        self.params["sigma_a"] = self.params["pool_active_stake"] / \
            self.params["total_active_stake"]

        self.params["beta"] = self.params["block_minted"] / \
            self.params["total_blocks"]
        try:
            self.params["pool_perf"] = self.params["beta"] / \
                self.params["sigma_a"]
        except ZeroDivisionError:
            self.params["pool_perf"] = "Pool active stake 0"
