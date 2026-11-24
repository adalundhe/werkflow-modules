from __future__ import annotations
from pydantic import BaseModel, StrictInt


class MSKS3DestinationUpdate(BaseModel):
    DataFreshnessInSeconds: StrictInt
