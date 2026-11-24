from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneAddRoleToDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr
    RoleArn: StrictStr
    FeatureName: StrictStr | None = None
