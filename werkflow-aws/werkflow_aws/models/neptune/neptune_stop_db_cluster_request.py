from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneStopDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr
