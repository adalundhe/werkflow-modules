from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DynamoDBOnDemandThroughput(BaseModel):
    MaxReadRequestUnits: StrictInt | None = None
    MaxWriteRequestUnits: StrictInt | None = None
