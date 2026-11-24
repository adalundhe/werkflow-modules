from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DynamoDBWarmThroughput(BaseModel):
    ReadUnitsPerSecond: StrictInt | None = None
    WriteUnitsPerSecond: StrictInt | None = None
