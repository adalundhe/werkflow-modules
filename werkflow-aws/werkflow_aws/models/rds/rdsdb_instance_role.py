from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDBInstanceRole(BaseModel):
    RoleArn: StrictStr | None = None
    FeatureName: StrictStr | None = None
    Status: StrictStr | None = None
