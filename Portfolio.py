# -*- coding: utf-8 -*-
"""
The Portfolio
"""

import os
import pickle
import Assets
import Savingplan


class portfolio(object):

    def __init__(self):
        self.assets = []
        self.savingplans = []
        self.cashflow = 0

    def add_asset(self, type, price, rendite):
        self.assets.append(Assets.asset.factory(type, price, rendite))
        
    def add_savingplan(self, plan):
        self.savingplans.append(plan)   
        
    def get_value(self, date=None):
        """ Some parsingtrouble here! """
        if not date:
            return sum(x.estimated_return() for x in self.assets)
        elif isinstance(date, str): 
            date = Assets.dateutil.parser.parse(date).date()
            return sum(x.estimated_return(date) for x in self.assets)
        else:
            return sum(x.estimated_return(date) for x in self.assets)

    def calculate_value(self, date):
        """ Uses the actual portfolio and all savingplans to calculate your money"""
        s = Assets.datetime.date.today()
        enddate = Assets.dateutil.parser.parse(date).date()
        delta = Assets.dateutil.relativedelta.relativedelta(months=+1)
        while s <= enddate:
            print(s)
            for p in self.savingplans:
                #new_asset = p.excercise() #TODO thios is to come
                #new_asset.bdate = s
                #self.assets.append(new_asset)
                self.add_asset("ETF_Thes", 1000, 0.05)
            print(self.assets)
            print(self.get_value(s))
            s += delta
         
    def save_portfolio(self, filename):
        filename += ".pkl"
        if not os.path.exists(filename):
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        else:
            print("File {} already exists".format(filename))
        
    @staticmethod
    def load_portfolio(filename):
        filename += ".pkl"
        if os.path.exists(filename):
            with open(filename, "rb") as file:
                return pickle.load(file)
        else:
            print(filename + " does not exist!")


if __name__ == "__main__":
    a = portfolio()
    a.add_asset("Real_Estate", 100000, 0.1)
    a.save_portfolio("test")
    
    b = portfolio.load_portfolio("test")
    os.remove("test.pkl")
    
    assert a.get_value() == 100000

    #p = Savingplan.savingplan()
    a.add_savingplan("Test")

    a.calculate_value("4 Dec 2025")




