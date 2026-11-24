from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDeleteGlobalClusterRequest(BaseModel):
    GlobalClusterIdentifier: StrictStr
