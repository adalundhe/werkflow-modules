from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EC2DescribeAccountVpcEncryptionControlRequest(BaseModel):
    DryRun: StrictBool | None = None
