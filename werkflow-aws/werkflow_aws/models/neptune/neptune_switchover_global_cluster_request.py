from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneSwitchoverGlobalClusterRequest(BaseModel):
    GlobalClusterIdentifier: StrictStr
    TargetDbClusterIdentifier: StrictStr
