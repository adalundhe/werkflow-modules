from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubPermissionModel(BaseModel):
    crossAccountRoleArns: list[StrictStr] | None = None
    invokerRoleName: StrictStr | None = None
    type: StrictStr | None = None
