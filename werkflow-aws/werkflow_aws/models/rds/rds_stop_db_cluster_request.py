from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSStopDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr
