from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSPromoteReadReplicaDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr
