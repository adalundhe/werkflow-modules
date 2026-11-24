from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSSwitchoverReadReplicaRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
