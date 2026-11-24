from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSSwitchoverGlobalClusterRequest(BaseModel):
    GlobalClusterIdentifier: StrictStr
    TargetDbClusterIdentifier: StrictStr
