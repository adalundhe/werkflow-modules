from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EC2ModifyHostsRequest(BaseModel):
    HostIds: list[StrictStr]
    HostRecovery: Literal['on', 'off'] | None = None
    InstanceType: StrictStr | None = None
    InstanceFamily: StrictStr | None = None
    HostMaintenance: Literal['on', 'off'] | None = None
    AutoPlacement: Literal['on', 'off'] | None = None
