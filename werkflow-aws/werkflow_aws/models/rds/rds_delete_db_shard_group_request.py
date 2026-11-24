from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDeleteDBShardGroupRequest(BaseModel):
    DBShardGroupIdentifier: StrictStr
