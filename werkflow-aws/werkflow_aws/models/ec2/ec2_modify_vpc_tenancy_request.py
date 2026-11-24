from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyVpcTenancyRequest(BaseModel):
    VpcId: StrictStr
    InstanceTenancy: Literal['default']
    DryRun: StrictBool | None = None
