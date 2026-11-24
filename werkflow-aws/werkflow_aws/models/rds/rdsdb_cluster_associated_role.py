from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDBClusterAssociatedRole(BaseModel):
    RoleArn: StrictStr
    FeatureName: StrictStr | None = None
