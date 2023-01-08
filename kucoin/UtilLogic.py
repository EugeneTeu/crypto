

import json
import pprint
from types import SimpleNamespace

from TickerInfo import TickerInfo


class UtilLogic:
    
    @staticmethod
    def measure(prev_price: float, current_price: float):
        try:
            percentageChange = (abs(current_price - prev_price) / prev_price) * 100.0
            val = f'+{percentageChange:.5f}%'if percentageChange > 0 else f'-{percentageChange:.5f}%'
            print(val)
            return current_price
        except ZeroDivisionError:
            return prev_price
    
    @staticmethod
    def getInfoFromFile(tickerName: str) -> TickerInfo:
        try:
            with open(f'{tickerName}.json','r') as openFile:
                json_object = json.load(openFile)
                return TickerInfo(tickerName=tickerName, tickerInfo=json_object)
        except FileNotFoundError:
            return TickerInfo(tickerName=tickerName, tickerInfo=None)

    @staticmethod
    def saveToFile(tickerName: str, tickerInfo: TickerInfo):
        json_data = json.dumps(tickerInfo, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
        with open(f"{tickerName}.json", "w") as outfile:
            outfile.write(json_data)
        return