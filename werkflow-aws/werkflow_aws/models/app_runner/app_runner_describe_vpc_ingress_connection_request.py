from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerDescribeVpcIngressConnectionRequest(BaseModel):
    VpcIngressConnectionArn: StrictStr
