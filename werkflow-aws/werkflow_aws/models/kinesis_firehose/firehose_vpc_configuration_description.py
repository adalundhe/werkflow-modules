from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehoseVpcConfigurationDescription(BaseModel):
    SubnetIds: list[StrictStr] | None = None
    RoleARN: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    VpcId: StrictStr | None = None
