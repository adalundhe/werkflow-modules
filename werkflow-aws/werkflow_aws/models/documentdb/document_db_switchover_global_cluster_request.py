from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBSwitchoverGlobalClusterRequest(BaseModel):
    GlobalClusterIdentifier: StrictStr
    TargetDbClusterIdentifier: StrictStr
