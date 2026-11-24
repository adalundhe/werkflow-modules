from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDeleteDBClusterEndpointRequest(BaseModel):
    DBClusterEndpointIdentifier: StrictStr
