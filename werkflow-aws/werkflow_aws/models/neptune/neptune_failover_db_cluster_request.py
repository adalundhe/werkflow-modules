from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneFailoverDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr | None = None
    TargetDBInstanceIdentifier: StrictStr | None = None
