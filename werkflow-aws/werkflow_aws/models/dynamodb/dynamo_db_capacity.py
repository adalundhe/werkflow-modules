from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class DynamoDBCapacity(BaseModel):
    ReadCapacityUnits: StrictFloat | StrictInt | None = None
    WriteCapacityUnits: StrictFloat | StrictInt | None = None
    CapacityUnits: StrictFloat | StrictInt | None = None
