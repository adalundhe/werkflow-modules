from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GuardDutyEksCluster(BaseModel):
    Arn: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    VpcId: StrictStr | None = None
    Ec2InstanceUids: list[StrictStr] | None = None
