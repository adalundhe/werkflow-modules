from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneRemoveFromGlobalClusterRequest(BaseModel):
    GlobalClusterIdentifier: StrictStr
    DbClusterIdentifier: StrictStr
