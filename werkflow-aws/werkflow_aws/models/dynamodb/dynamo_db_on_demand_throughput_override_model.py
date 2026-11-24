from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DynamoDBOnDemandThroughputOverrideModel(BaseModel):
    MaxReadRequestUnits: StrictInt | None = None
