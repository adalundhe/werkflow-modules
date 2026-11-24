from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class SSMRegisterDefaultHostManagementConfigurationRequest(BaseModel):
    PermissionModel: Literal['SERVICE_MANAGED', 'SELF_MANAGED']
    RoleArn: StrictStr | None = None
    Overwrite: StrictBool | None = None
