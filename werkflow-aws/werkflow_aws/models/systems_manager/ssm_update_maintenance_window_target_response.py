from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_target import SSMTarget


class SSMUpdateMaintenanceWindowTargetResponse(BaseModel):
    WindowId: StrictStr | None = None
    WindowTargetId: StrictStr | None = None
    Targets: list[SSMTarget] | None = None
    OwnerInformation: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
