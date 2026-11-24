from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DynamoDBEndpoint(BaseModel):
    Address: StrictStr | None = None
    CachePeriodInMinutes: StrictInt | None = None
