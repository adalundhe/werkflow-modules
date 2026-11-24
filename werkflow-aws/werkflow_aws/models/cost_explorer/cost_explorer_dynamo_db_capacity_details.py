from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerDynamoDBCapacityDetails(BaseModel):
    CapacityUnits: StrictStr | None = None
    Region: StrictStr | None = None
