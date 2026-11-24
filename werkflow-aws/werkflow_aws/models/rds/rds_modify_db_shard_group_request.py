from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RDSModifyDBShardGroupRequest(BaseModel):
    DBShardGroupIdentifier: StrictStr
    MaxACU: StrictFloat | StrictInt | None = None
    MinACU: StrictFloat | StrictInt | None = None
    ComputeRedundancy: StrictInt | None = None
