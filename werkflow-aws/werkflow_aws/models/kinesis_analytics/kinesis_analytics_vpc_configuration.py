from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsVpcConfiguration(BaseModel):
    SubnetIds: list[StrictStr]
    SecurityGroupIds: list[StrictStr]
