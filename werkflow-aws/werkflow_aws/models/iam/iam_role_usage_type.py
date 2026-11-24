from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMRoleUsageType(BaseModel):
    Region: StrictStr | None = None
    Resources: list[StrictStr] | None = None
