from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDBClusterRoleModel(BaseModel):
    RoleArn: StrictStr | None = None
    Status: StrictStr | None = None
    FeatureName: StrictStr | None = None
