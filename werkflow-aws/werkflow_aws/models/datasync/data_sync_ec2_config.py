from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncEc2Config(BaseModel):
    SubnetArn: StrictStr | None = None
    SecurityGroupArns: list[StrictStr] | None = None
