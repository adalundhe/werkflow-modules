from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneDeleteGlobalClusterRequest(BaseModel):
    GlobalClusterIdentifier: StrictStr
