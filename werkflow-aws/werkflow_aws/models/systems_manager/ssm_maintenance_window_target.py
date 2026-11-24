from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_target import SSMTarget


class SSMMaintenanceWindowTarget(BaseModel):
    WindowId: StrictStr | None = None
    WindowTargetId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Targets: list[SSMTarget] | None = None
    OwnerInformation: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
