from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDBClusterAssociatedRoleModel(BaseModel):
    RoleArn: StrictStr
    FeatureName: StrictStr | None = None
