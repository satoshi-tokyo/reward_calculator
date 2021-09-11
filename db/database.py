import sqlite3


class Database(object):
    def __init__(self):
        self.dbname = "sqlite3.db"
        self.network_supply_table = "network_supply"
        self.network_stake_table = "network_stake"
        self.pool_table = "pool"
        self.conn = sqlite3.connect(self.dbname)
        self.cur = self.conn.cursor()

    def createdb(self):
        cmd = "CREATE TABLE IF NOT EXISTS {}(epoch INTEGER, max INTEGER, total INTEGER, circulating INTEGER)".format(
            self.network_supply_table)
        self.cur.execute(cmd)
        cmd = "CREATE TABLE IF NOT EXISTS {}(epoch INTEGER, live INTEGER, active INTEGER)".format(
            self.network_stake_table)
        self.cur.execute(cmd)
        cmd = "CREATE TABLE IF NOT EXISTS {}(epoch INTEGER, live_stake INTEGER, active_stake INTEGER, declared_pledge INTEGER, live_pledge INTEGER, margin_cost REAL, fixed_cost INTEGER )".format(
            self.pool_table)
        self.cur.execute(cmd)

    def insert_network_supply(self, epoch, network_data):
        # print(epoch)
        # print(network_data)
        # Check information of the epoch already exists in the table
        cmd = "INSERT INTO {} VALUES (?,?,?,?)".format(
            self.network_supply_table)
        self.cur.execute(cmd, (epoch, network_data["supply"]["max"],
                         network_data["supply"]["total"], network_data["supply"]["circulating"]))
        self.conn.commit()

    def update_network_supply(self, epoch, network_data):
        # print(epoch)
        # print(network_data)
        # Check information of the epoch already exists in the table

        cmd = "UPDATE {} SET total=?,circulating=? WHERE epoch=?".format(
            self.network_supply_table)
        self.cur.execute(
            cmd, (network_data["supply"]["total"], network_data["supply"]["circulating"], epoch))
        self.conn.commit()

    def insert_network_stake(self, epoch, network_data):
        cmd = "INSERT INTO {} VALUES (?,?,?)".format(
            self.network_stake_table)
        self.cur.execute(
            cmd, (epoch, network_data["stake"]["live"], network_data["stake"]["active"]))
        self.conn.commit()

    def update_network_stake(self, epoch, network_data):
        cmd = "UPDATE {} SET live=? WHERE epoch=?".format(
            self.network_stake_table)
        self.cur.execute(
            cmd, (network_data["stake"]["live"], epoch))
        self.conn.commit()

    def insert_pool(self, epoch, pool_data):
        cmd = "INSERT INTO {} VALUES (?,?,?,?,?,?,?)".format(
            self.pool_table)
        self.cur.execute(
            cmd, (epoch, pool_data["live_stake"], pool_data["active_stake"], pool_data["declared_pledge"], pool_data["live_pledge"], pool_data["margin_cost"], pool_data["fixed_cost"]))
        self.conn.commit()

    def update_pool(self, epoch, pool_data):
        cmd = "UPDATE {} SET live_stake=?,active_stake=?,declared_pledge=?,live_pledge=?,margin_cost=?,fixed_cost=? WHERE epoch=?".format(
            self.pool_table)

        self.cur.execute(
            cmd, (pool_data["live_stake"], pool_data["active_stake"], pool_data["declared_pledge"], pool_data["live_pledge"], pool_data["margin_cost"], pool_data["fixed_cost"], epoch))
        self.conn.commit()

    def select_if_epoch_exits(self, table, epoch):
        """
            Returns: count of data
        """
        cmd = "SELECT count(*) FROM {} WHERE epoch=?".format(table)
        data = (epoch,)
        self.cur.execute(cmd, data)
        out = self.cur.fetchone()
        return int(out[0])

    def select_from_network_supply_table(self, epoch):
        """
        Returns: epoch, max, total, circulating

        """
        cmd = "SELECT * FROM {} WHERE epoch=?".format(
            self.network_supply_table)
        data = (epoch,)

        self.cur.execute(cmd, data)
        out = self.cur.fetchall()
        return out[0]

    def select_from_pool_table(self, epoch):
        """
        Returns: epoch,live_stake, active_stake, declared_pledge, live_pledge, margin_cost, fixed_cost

        """
        cmd = "SELECT * FROM {} WHERE epoch=?".format(
            self.pool_table)
        data = (epoch,)

        self.cur.execute(cmd, data)
        out = self.cur.fetchone()
        return out

    def _select(self):
        print(f'{"="*50}')
        print(f'epoch, max, total, circulating')
        cmd = "SELECT * FROM {}".format(self.network_supply_table)
        self.cur.execute(cmd)
        out = self.cur.fetchall()

        for row in out:
            print(row[0], row[1], row[2], row[3])

        print(f'{"="*50}')
        print(f'epoch, live, active')
        cmd = "SELECT * FROM {}".format(self.network_stake_table)
        self.cur.execute(cmd)
        out = self.cur.fetchall()

        for row in out:
            print(row[0], row[1], row[2])

        print(f'{"="*50}')
        print(f'epoch,live_stake, active_stake, declared_pledge, live_pledge, margin_cost, fixed_cost')
        cmd = "SELECT * FROM {}".format(self.pool_table)
        self.cur.execute(cmd)
        out = self.cur.fetchall()

        for row in out:
            print(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

    def close_db(self):
        self.conn.close()
