from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamVpcConfig(BaseModel):
    SubnetIds: list[StrictStr] | None = None
    SecurityGroupIds: list[StrictStr] | None = None
