from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt


class DynamoDBDescribeLimitsResponse(BaseModel):
    AccountMaxReadCapacityUnits: StrictInt | None = None
    AccountMaxWriteCapacityUnits: StrictInt | None = None
    TableMaxReadCapacityUnits: StrictInt | None = None
    TableMaxWriteCapacityUnits: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
