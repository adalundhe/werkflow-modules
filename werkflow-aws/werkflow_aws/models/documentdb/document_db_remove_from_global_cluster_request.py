from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBRemoveFromGlobalClusterRequest(BaseModel):
    GlobalClusterIdentifier: StrictStr
    DbClusterIdentifier: StrictStr
