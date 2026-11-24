from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EC2DescribeVpcBlockPublicAccessOptionsRequest(BaseModel):
    DryRun: StrictBool | None = None
