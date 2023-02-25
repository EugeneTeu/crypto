from typing import List
from typing import Any
from dataclasses import dataclass
import json


@dataclass
class Changes:
    asks: List[str]  # price, size , sequence
    bids: List[str]

    @staticmethod
    def from_dict(obj: Any) -> "Changes":
        _asks = [y for y in obj.get("asks")]
        _bids = [y for y in obj.get("bids")]
        return Changes(_asks, _bids)


@dataclass
class Data:
    changes: Changes
    sequenceEnd: float
    sequenceStart: float
    symbol: str
    time: float

    @staticmethod
    def from_dict(obj: Any) -> "Data":
        _changes = Changes.from_dict(obj.get("changes"))
        _sequenceEnd = float(obj.get("sequenceEnd"))
        _sequenceStart = float(obj.get("sequenceStart"))
        _symbol = str(obj.get("symbol"))
        _time = float(obj.get("time"))
        return Data(_changes, _sequenceEnd, _sequenceStart, _symbol, _time)


@dataclass
class Level2MarketDataMsg:
    type: str
    topic: str
    subject: str
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> "Level2MarketDataMsg":
        _type = str(obj.get("type"))
        _topic = str(obj.get("topic"))
        _subject = str(obj.get("subject"))
        _data = Data.from_dict(obj.get("data"))
        return Level2MarketDataMsg(_type, _topic, _subject, _data)


# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Level2MarketDataMsg.from_dict(jsonstring)
# https://json2csharp.com/code-converters/json-to-python
