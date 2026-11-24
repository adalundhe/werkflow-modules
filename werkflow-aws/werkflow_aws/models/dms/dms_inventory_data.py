from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DMSInventoryData(BaseModel):
    NumberOfDatabases: StrictInt | None = None
    NumberOfSchemas: StrictInt | None = None
