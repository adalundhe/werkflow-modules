from __future__ import annotations
from pydantic import BaseModel, StrictInt


class MSKIcebergDestinationUpdate(BaseModel):
    DataFreshnessInSeconds: StrictInt
