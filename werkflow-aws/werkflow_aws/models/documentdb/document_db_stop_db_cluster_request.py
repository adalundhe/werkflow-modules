from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBStopDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr
