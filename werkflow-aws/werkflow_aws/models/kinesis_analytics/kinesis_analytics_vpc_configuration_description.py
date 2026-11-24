from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsVpcConfigurationDescription(BaseModel):
    VpcConfigurationId: StrictStr | None = None
    VpcId: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
    SecurityGroupIds: list[StrictStr] | None = None
