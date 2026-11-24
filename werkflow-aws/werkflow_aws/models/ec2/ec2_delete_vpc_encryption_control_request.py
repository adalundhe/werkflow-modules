from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteVpcEncryptionControlRequest(BaseModel):
    VpcEncryptionControlId: StrictStr
    DryRun: StrictBool | None = None
