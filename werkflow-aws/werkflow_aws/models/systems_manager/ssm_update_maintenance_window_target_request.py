from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ssm_target import SSMTarget


class SSMUpdateMaintenanceWindowTargetRequest(BaseModel):
    WindowId: StrictStr
    WindowTargetId: StrictStr
    Targets: list[SSMTarget] | None = None
    OwnerInformation: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Replace: StrictBool | None = None
