from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DynamoDBProvisionedThroughputOverrideModel(BaseModel):
    ReadCapacityUnits: StrictInt | None = None
