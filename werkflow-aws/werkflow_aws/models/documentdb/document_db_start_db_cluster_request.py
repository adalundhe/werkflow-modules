from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBStartDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr
