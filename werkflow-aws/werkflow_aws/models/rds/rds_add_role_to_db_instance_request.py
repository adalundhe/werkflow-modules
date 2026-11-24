from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSAddRoleToDBInstanceRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
    RoleArn: StrictStr
    FeatureName: StrictStr
