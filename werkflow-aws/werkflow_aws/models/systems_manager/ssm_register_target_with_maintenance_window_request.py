from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ssm_target import SSMTarget


class SSMRegisterTargetWithMaintenanceWindowRequest(BaseModel):
    WindowId: StrictStr
    ResourceType: Literal['INSTANCE', 'RESOURCE_GROUP']
    Targets: list[SSMTarget]
    OwnerInformation: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    ClientToken: StrictStr | None = None
