from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSFailoverDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr
    TargetDBInstanceIdentifier: StrictStr | None = None
