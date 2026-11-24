from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DynamoDBWarmThroughputModel(BaseModel):
    ReadUnitsPerSecond: StrictInt | None = None
    WriteUnitsPerSecond: StrictInt | None = None
