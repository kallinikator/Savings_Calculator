# -*- coding: utf-8 -*-
"""
This is a planner for your financial assets and your estimated returns
"""

import datetime
import dateutil


class asset(object):
    
    tax = 0.25
    
    def __init__(self, price, rendite):
        self.price = price
        self.rendite = rendite
        self.bdate = datetime.date.today()
        
    def __repr__(self):
        return "{}, price: {}".format(self.__class__.__name__, self.price)
            
    def set_date(self, new_date):
        self.bdate = dateutil.parser.parse(new_date).date()
        
    def estimated_return(self, date=datetime.date.today()):
        if isinstance(date, str):
            date = dateutil.parser.parse(date).date()
        time_hold = date - self.bdate
        return self.price * (1 + self.rendite * (1 - asset.tax)) ** (time_hold.days / 365)
        
    @staticmethod
    def factory(type, price, rendite):
        if type == "Real_Estate": return real_estate(price, rendite)
        if type == "ETF_Thes": return etf_thes(price, rendite)
        assert 0, "Bad asset: " + type
            
    
class real_estate(asset):
    """ A real_estate object """
    
    @staticmethod
    def calculate_leverage(price, costs, equity):
        return price * costs / equity
        
class etf_thes(asset):
    """ A classic asset """
    pass
        
        
if __name__ == "__main__":
    a = asset.factory("Real_Estate", 10, 0.03)
    a.set_date("01.01.1991")
    assert a.bdate == dateutil.parser.parse("01.01.1991").date()
    assert a.estimated_return("01.01.1992") == 10.225
