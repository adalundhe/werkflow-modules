from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehoseVpcConfiguration(BaseModel):
    SubnetIds: list[StrictStr]
    RoleARN: StrictStr
    SecurityGroupIds: list[StrictStr]
