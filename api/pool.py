import json
import requests

from api import settings

POOL_ID = settings.POOL_ID
PROJECT_ID = settings.PROJECT_ID
HEADERS = {"project_id": PROJECT_ID}


class Pool(object):
    def __init__(self, epoch=""):
        self.mainnet_url = 'https://cardano-mainnet.blockfrost.io/api/v0'
        self.epoch = epoch
        self.pool_list = []
        self.pool_info_list = []

    def specific_pool(self, ext_pool_id=""):
        """
        Returns(dict): response
        Example: {"pool_id":"pool1tjr4zpndkvwkw3du3fvt59f5men6jhuevt7rpx6xw0wcct5kl04","hex":"5c8751066db31d6745bc8a58ba1534de67a95f9962fc309b4673dd8c","vrf_key":"66cf45520d4aa810ba6360bd8d42d2325cbef6112efee50e4233edb97cc1b26e","blocks_minted":414,"live_stake":"10187152600183","live_size":0.0004371068199031763,"live_saturation":0.15522070629496273,"live_delegators":90,"active_stake":"9283494841935","active_size":0.0004012536869197099,"declared_pledge":"50000000000","live_pledge":"59599853318","margin_cost":0.009,"fixed_cost":"340000000","reward_account":"stake1u84fcl0zp64ymt5jyuje8dszqekzk4ym59ew2cd59hsraegpp6x6k","owners":["stake1u84fcl0zp64ymt5jyuje8dszqekzk4ym59ew2cd59hsraegpp6x6k"],"registration":["08275ce0bc949681da22cfbb24d6c2fe19f8d6354ad9b11960bbb3099b5093e4","e13b5cdf01413ee58af0feeb3775be9e26fb79d71c809aa0793e4860c1d42758","4c2a8a212445d8e846f0a0281bef8dd2161fd34f59a3d0d8d2c7ba8d8846b980","7301757480653cda868d5c4ef14e2ae9277ba596049df183d604530f21f3f8ea","6fb9211f75a42187db70446d0549baac66d09e407d3fa0a5767f81b142273c42","e5491fe1761b2307e85fe7bbd92bb862d09be6c8d82b83c824f64b3a42a37d19","dd22548e7d628485c5fde5cb2a96ad499ea90caf04467cd61cee560bc7c58c7a","4c6ac0c998339d402414e4273d64e705d2752e94e1ed671669cc8ce5329b8fef","e6ccd5a4820cfb7ccd87a3ae84f6dbcd17af99e379292d41fac012ccaa4ee59c","14626821fc71933fb494a4d619f3a5b2f540934ddcee82a9b11915484a8505b8","4fe072a65b7dc832d15b489b74f3ee5463fe1984a82d2bbf1abb32cc966bfe68","31bae21745cee5330b8bbb74f7ae2110a435e7f55a63b913a0f4e6b85b92e8b1","21f041b7f322efc790f740fd2e74881c3760502b7588013a4f1fe8dbb122cb11","df1ba84dc121e7644932aae1769a125189e880f1d5a0a0f4e3c3c01db11ce36c"],"retirement":[]}
        """
        if ext_pool_id:
            url = self.mainnet_url + "/pools/" + ext_pool_id
        else:
            url = self.mainnet_url + "/pools/" + POOL_ID
        response = requests.get(url, headers=HEADERS)
        return json.loads(response.text)

    def pool_list_all(self):
        page = 1
        while True:
            url = self.mainnet_url + "/pools?page={}".format(page)
            response = requests.get(url, headers=HEADERS)
            _new_pool_list = []
            _new_pool_list = json.loads(response.text)
            self.pool_list.extend(_new_pool_list)
            page += 1
            # # Dev purpose
            # if page == 2:
            #     break
            if _new_pool_list == []:
                break

    def pool_historical_data(self, epoch="", ext_pool_id=""):
        """
            Returns:
            data(dict): pool stats of epoch specified. 
                e.g.,{'epoch': 289, 'blocks': 47, 'active_stake': '48628324341765', 'active_size': 0.00208605009883614, 'delegators_count': 1877, 'rewards': '33625029705', 'fees': '639565267'}
        """
        if ext_pool_id:
            url = self.mainnet_url + "/pools/" + ext_pool_id + "/history"
        else:
            url = self.mainnet_url + "/pools/" + POOL_ID + "/history"
        response = requests.get(url, headers=HEADERS)
        if epoch:
            for data in json.loads(response.text):
                if data["epoch"] == epoch:
                    return data
        else:
            return json.loads(response.text)
        return {"status": "Epoch data not found", "message": "Pool might be too new to have epoch {} data".format(epoch)}
