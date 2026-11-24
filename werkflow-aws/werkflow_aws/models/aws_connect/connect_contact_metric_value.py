from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class ConnectContactMetricValue(BaseModel):
    Number: StrictFloat | StrictInt | None = None
