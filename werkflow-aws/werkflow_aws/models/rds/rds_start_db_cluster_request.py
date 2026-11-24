from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSStartDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr
