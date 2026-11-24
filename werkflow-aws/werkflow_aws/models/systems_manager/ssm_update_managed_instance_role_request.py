from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMUpdateManagedInstanceRoleRequest(BaseModel):
    InstanceId: StrictStr
    IamRole: StrictStr
