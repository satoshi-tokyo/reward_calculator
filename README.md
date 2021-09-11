# reward_calculator

## settings.py
Under `api` folder, place settings.py with `POOL_ID` and `PROJECT_ID`, e.g.,
```
POOL_ID = "poolxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Pool id
PROJECT_ID = "XXXXXXXXXXXXXXXXXXXXXXXXXX"  # Project API Key from Blockfrost
```

## Command options
-help option 
```
$ python reward.py -h
usage: reward.py [-h] [-epoch EPOCH] [-stake STAKE]

optional arguments:
  -h, --help    show this help message and exit
  -epoch EPOCH  specify epoch you want to know reward of. Default is current epoch.
  -stake STAKE  specify stake amount you are delegating in ADA.
  -db           retrieves data, store into database and outputs
```

Run with no option  
- epoch is set to the latest epoch and calculates with data 2 epochs before
- writes data into a `json/data.json` file 

-db option  
- retrieves data from Blockfrost and inserts into sqlite3  
- outputs data from db (will be removed)  

-epoch option  
- calculates reward delivered to pool of pool id specified in setting.py at given epoch (calculated with data 2 epoch before). Certain data like `live_pledge` and `total_supply` need to be in database as they change over epoch.  
- writes data into a `json/e{epoch}.json` file where {epoch} is calculated epoch, i.e., if current epoch: 290, calculated epoch: 288. 

-stake option
- calculates reward of given active stake amount, i.e., delegator's reward.

```
$ python reward.py -epoch 290 -stake 40000
Reward: 16.762797353014584 ADA
```
