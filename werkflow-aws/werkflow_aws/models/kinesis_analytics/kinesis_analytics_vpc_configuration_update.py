from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsVpcConfigurationUpdate(BaseModel):
    VpcConfigurationId: StrictStr
    SubnetIdUpdates: list[StrictStr] | None = None
    SecurityGroupIdUpdates: list[StrictStr] | None = None
