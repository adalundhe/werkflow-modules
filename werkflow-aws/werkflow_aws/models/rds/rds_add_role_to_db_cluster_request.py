from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSAddRoleToDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr
    RoleArn: StrictStr
    FeatureName: StrictStr | None = None
