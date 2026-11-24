from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerRoleGroupAssignment(BaseModel):
    RoleName: StrictStr | None = None
    GroupPatterns: list[StrictStr] | None = None
