from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DynamoDBProvisionedThroughput(BaseModel):
    ReadCapacityUnits: StrictInt
    WriteCapacityUnits: StrictInt
