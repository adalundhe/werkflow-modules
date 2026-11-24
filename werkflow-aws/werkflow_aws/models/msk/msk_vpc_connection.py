from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class MSKVpcConnection(BaseModel):
    VpcConnectionArn: StrictStr | None = None
    TargetClusterArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Authentication: StrictStr | None = None
    VpcId: StrictStr | None = None
    State: StrictStr | None = None
