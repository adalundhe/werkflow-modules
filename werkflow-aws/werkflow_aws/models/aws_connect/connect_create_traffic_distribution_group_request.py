from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectCreateTrafficDistributionGroupRequest(BaseModel):
    Name: StrictStr
    InstanceId: StrictStr
    Description: StrictStr | None = None
    ClientToken: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
