from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DynamoDBProvisionedThroughputModel(BaseModel):
    ReadCapacityUnits: StrictInt | None = None
    WriteCapacityUnits: StrictInt | None = None
