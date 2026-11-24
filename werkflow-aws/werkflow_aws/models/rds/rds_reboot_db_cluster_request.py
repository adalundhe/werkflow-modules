from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSRebootDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr
