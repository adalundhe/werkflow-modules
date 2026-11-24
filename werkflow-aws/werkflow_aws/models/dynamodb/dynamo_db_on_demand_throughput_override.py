from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DynamoDBOnDemandThroughputOverride(BaseModel):
    MaxReadRequestUnits: StrictInt | None = None
