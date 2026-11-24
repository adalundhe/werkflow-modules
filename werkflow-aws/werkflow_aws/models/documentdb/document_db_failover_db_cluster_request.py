from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBFailoverDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr | None = None
    TargetDBInstanceIdentifier: StrictStr | None = None
