from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt


class DynamoDBProvisionedThroughputDescription(BaseModel):
    LastIncreaseDateTime: datetime.datetime | None = None
    LastDecreaseDateTime: datetime.datetime | None = None
    NumberOfDecreasesToday: StrictInt | None = None
    ReadCapacityUnits: StrictInt | None = None
    WriteCapacityUnits: StrictInt | None = None
