# reward_calculator

## settings.py
Under `api` folder, place settings.py with `POOL_ID` and `PROJECT_ID`, e.g.,
```
POOL_ID = "poolxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Pool id
PROJECT_ID = "XXXXXXXXXXXXXXXXXXXXXXXXXX"  # Project API Key from Blockfrost
```

## Command options - reward.py
-help option 
```
$ python reward.py -h
usage: reward.py [-h] [-epoch EPOCH] [-stake STAKE]

optional arguments:
  -h, --help    show this help message and exit
  -epoch EPOCH  specify epoch you want to know reward of. Default is current epoch.
  -stake STAKE  specify stake amount you are delegating in ADA.
  -simul SIMUL  to simulate with active_stake, pledge, etc..
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

-simul option
1. With `active_stake` as an argument, outputs a csv file with data active_stake_in_ada vs reward assuming 100K ADA is delegated.
Active stake varies between 1M and 100M, with step of 1M.
1. With `perf` as an argument, outputs a csv file with data active stake vs pool performance. (working) 
Get all pool data per epoch, calculates performance, and plots with active stake.
```
$ python reward.py -epoch 290 -stake 40000
Reward: 16.762797353014584 ADA
```

## Command options - pool_stats.py

```
$ python pool_stats.py -h
usage: pool_stats.py [-h] [-pool POOL]

optional arguments:
  -h, --help  show this help message and exit
  -pool POOL  retrieves data and outputs
```

`python pool_stats.py -pool all` will query data of all pools and outputs into a csv file.