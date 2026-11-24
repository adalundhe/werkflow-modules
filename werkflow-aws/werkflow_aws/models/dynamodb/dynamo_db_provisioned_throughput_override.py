from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DynamoDBProvisionedThroughputOverride(BaseModel):
    ReadCapacityUnits: StrictInt | None = None
