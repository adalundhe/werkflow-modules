from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class EC2ModifyInstancePlacementRequest(BaseModel):
    InstanceId: StrictStr
    GroupName: StrictStr | None = None
    PartitionNumber: StrictInt | None = None
    HostResourceGroupArn: StrictStr | None = None
    GroupId: StrictStr | None = None
    Tenancy: Literal['default', 'dedicated', 'host'] | None = None
    Affinity: Literal['default', 'host'] | None = None
    HostId: StrictStr | None = None
