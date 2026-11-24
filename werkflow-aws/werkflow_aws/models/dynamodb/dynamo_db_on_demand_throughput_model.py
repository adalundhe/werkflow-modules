from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DynamoDBOnDemandThroughputModel(BaseModel):
    MaxReadRequestUnits: StrictInt | None = None
    MaxWriteRequestUnits: StrictInt | None = None
