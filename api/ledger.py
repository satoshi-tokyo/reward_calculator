import json
import requests

from api import settings


POOL_ID = settings.POOL_ID
PROJECT_ID = settings.PROJECT_ID
HEADERS = {"project_id": PROJECT_ID}


class Ledger(object):
    def __init__(self, epoch=""):
        self.mainnet_url = 'https://cardano-mainnet.blockfrost.io/api/v0'
        self.epoch = str(epoch)

    def latest_epoch(self):
        url = self.mainnet_url + '/epochs/latest'
        response = requests.get(url, headers=HEADERS)
        return json.loads(response.text)

    def epoch_stats(self):
        """
            {
                "epoch": 225,
                "start_time": 1603403091,
                "end_time": 1603835086,
                "first_block_time": 1603403092,
                "last_block_time": 1603835084,
                "block_count": 21298,
                "tx_count": 17856,
                "output": "7849943934049314",
                "fees": "4203312194",
                "active_stake": "784953934049314"
            }
        """

        url = self.mainnet_url + '/epochs/' + self.epoch
        response = requests.get(url, headers=HEADERS)
        return json.loads(response.text)

    def network(self):
        url = self.mainnet_url + '/network/'
        response = requests.get(url, headers=HEADERS)
        return json.loads(response.text)

    def parameters(self):
        """
            {
                "epoch": 225,
                "min_fee_a": 44,
                "min_fee_b": 155381,
                "max_block_size": 65536,
                "max_tx_size": 16384,
                "max_block_header_size": 1100,
                "key_deposit": "2000000",
                "pool_deposit": "500000000",
                "e_max": 18,
                "n_opt": 150,
                "a0": 0.3,
                "rho": 0.003,
                "tau": 0.2,
                "decentralisation_param": 0.5,
                "extra_entropy": null,
                "protocol_major_ver": 2,
                "protocol_minor_ver": 0,
                "min_utxo": "1000000",
                "min_pool_cost": "340000000",
                "nonce": "1a3be38bcbb7911969283716ad7aa550250226b76a61fc51cc9a9a35d9276d81"
            }
        """
        url = self.mainnet_url + '/epochs/' + self.epoch + '/parameters'
        response = requests.get(url, headers=HEADERS)
        return json.loads(response.text)

    def pool_params(self):
        """
        Returns(dict): response
        Example: {"pool_id":"pool1tjr4zpndkvwkw3du3fvt59f5men6jhuevt7rpx6xw0wcct5kl04","hex":"5c8751066db31d6745bc8a58ba1534de67a95f9962fc309b4673dd8c","vrf_key":"66cf45520d4aa810ba6360bd8d42d2325cbef6112efee50e4233edb97cc1b26e","blocks_minted":414,"live_stake":"10187152600183","live_size":0.0004371068199031763,"live_saturation":0.15522070629496273,"live_delegators":90,"active_stake":"9283494841935","active_size":0.0004012536869197099,"declared_pledge":"50000000000","live_pledge":"59599853318","margin_cost":0.009,"fixed_cost":"340000000","reward_account":"stake1u84fcl0zp64ymt5jyuje8dszqekzk4ym59ew2cd59hsraegpp6x6k","owners":["stake1u84fcl0zp64ymt5jyuje8dszqekzk4ym59ew2cd59hsraegpp6x6k"],"registration":["08275ce0bc949681da22cfbb24d6c2fe19f8d6354ad9b11960bbb3099b5093e4","e13b5cdf01413ee58af0feeb3775be9e26fb79d71c809aa0793e4860c1d42758","4c2a8a212445d8e846f0a0281bef8dd2161fd34f59a3d0d8d2c7ba8d8846b980","7301757480653cda868d5c4ef14e2ae9277ba596049df183d604530f21f3f8ea","6fb9211f75a42187db70446d0549baac66d09e407d3fa0a5767f81b142273c42","e5491fe1761b2307e85fe7bbd92bb862d09be6c8d82b83c824f64b3a42a37d19","dd22548e7d628485c5fde5cb2a96ad499ea90caf04467cd61cee560bc7c58c7a","4c6ac0c998339d402414e4273d64e705d2752e94e1ed671669cc8ce5329b8fef","e6ccd5a4820cfb7ccd87a3ae84f6dbcd17af99e379292d41fac012ccaa4ee59c","14626821fc71933fb494a4d619f3a5b2f540934ddcee82a9b11915484a8505b8","4fe072a65b7dc832d15b489b74f3ee5463fe1984a82d2bbf1abb32cc966bfe68","31bae21745cee5330b8bbb74f7ae2110a435e7f55a63b913a0f4e6b85b92e8b1","21f041b7f322efc790f740fd2e74881c3760502b7588013a4f1fe8dbb122cb11","df1ba84dc121e7644932aae1769a125189e880f1d5a0a0f4e3c3c01db11ce36c"],"retirement":[]}
        """
        url = "https://cardano-mainnet.blockfrost.io/api/v0/pools/" + POOL_ID
        response = requests.get(url, headers=HEADERS)
        return json.loads(response.text)

    def pool_blocks_minted_per_epoch(self):
        """
            Returns(int): count of blocks minted
        """
        page = 1
        while True:
            url = "https://cardano-mainnet.blockfrost.io/api/v0/pools/" + \
                POOL_ID + "/history/?page={}".format(page)
            response = requests.get(url, headers=HEADERS)
            if response.text == []:
                break
            _epoch_info = []
            _epoch_info = [e for e in json.loads(response.text) if str(
                e['epoch']) == str(self.epoch)]
            if _epoch_info:
                epoch_info = _epoch_info[0]
                break
            page += 1
        return epoch_info['blocks']

    def reward_history(self, stake_address):
        """ Returns rewards history of given stake address.
            Args:
                stake_address(str): stake address
            Returns
                (list): list of rewards history
        """
        url = self.mainnet_url + "/accounts/" + stake_address + "/rewards"
        response = requests.get(url, headers=HEADERS)
        return json.loads(response.text)
