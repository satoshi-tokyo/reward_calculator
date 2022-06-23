import datetime

from api import ledger
from api import epochs


class Rewards(object):
    def __init__(self, stake_address="", epoch_start=0, epoch_end=""):
        self.stake_address = stake_address
        self.epoch_start = epoch_start
        self.epoch_end = epoch_end
        self.rewards_sum = 0
        self.ledger_obj = ledger.Ledger()

        if not epoch_end:
            _epoch_latest = self.ledger_obj.latest_epoch()
            self.epoch_end = _epoch_latest["epoch"]

    def list_rewards(self):
        """ This module retrieves rewards history.
        """
        self.rewards_list = self.ledger_obj.reward_history(self.stake_address)
        return self.rewards_list

    def add_rewards(self):
        """ This module adds rewards.
        """

        for r in self.rewards_list:
            if self.epoch_start <= r["epoch"] and self.epoch_end >= r["epoch"]:
                self.rewards_sum += int(r["amount"])

    def print_rewards(self):
        """ Prints rewards history with range of specified epochs.
        """
        for r in self.rewards_list:
            if self.epoch_start <= r["epoch"] and self.epoch_end >= r["epoch"]:
                print(r)
