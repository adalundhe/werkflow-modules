from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBDeleteGlobalClusterRequest(BaseModel):
    GlobalClusterIdentifier: StrictStr
