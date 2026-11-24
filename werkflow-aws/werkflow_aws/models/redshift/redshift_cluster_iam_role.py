from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftClusterIamRole(BaseModel):
    IamRoleArn: StrictStr | None = None
    ApplyStatus: StrictStr | None = None
