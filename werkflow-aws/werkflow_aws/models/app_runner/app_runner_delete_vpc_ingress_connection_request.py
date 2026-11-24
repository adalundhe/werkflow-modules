from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerDeleteVpcIngressConnectionRequest(BaseModel):
    VpcIngressConnectionArn: StrictStr
