from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneDeleteDBClusterEndpointRequest(BaseModel):
    DBClusterEndpointIdentifier: StrictStr
