from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RDSFailoverGlobalClusterRequest(BaseModel):
    GlobalClusterIdentifier: StrictStr
    TargetDbClusterIdentifier: StrictStr
    AllowDataLoss: StrictBool | None = None
    Switchover: StrictBool | None = None
