from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSRemoveFromGlobalClusterRequest(BaseModel):
    GlobalClusterIdentifier: StrictStr
    DbClusterIdentifier: StrictStr
