from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMDeregisterManagedInstanceRequest(BaseModel):
    InstanceId: StrictStr
