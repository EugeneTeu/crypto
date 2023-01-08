

import json
import pprint


class PriceLogic:
    

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
    def getPriceFromFile(ticker_name: str):
        try:
            with open(f'{ticker_name}.json','r') as openFile:
                json_object = json.load(openFile)
                return float(json_object[f'{ticker_name}'])
        except FileNotFoundError:
            print("file not found")
            return 0.0

