from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ConfirmProductInstanceRequest(BaseModel):
    InstanceId: StrictStr
    ProductCode: StrictStr
    DryRun: StrictBool | None = None
