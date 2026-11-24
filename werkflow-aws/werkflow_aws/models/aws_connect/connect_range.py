from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class ConnectRange(BaseModel):
    MinProficiencyLevel: StrictFloat | StrictInt | None = None
    MaxProficiencyLevel: StrictFloat | StrictInt | None = None
