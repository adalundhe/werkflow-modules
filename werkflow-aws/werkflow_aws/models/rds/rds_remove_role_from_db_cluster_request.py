from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSRemoveRoleFromDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr
    RoleArn: StrictStr
    FeatureName: StrictStr | None = None
