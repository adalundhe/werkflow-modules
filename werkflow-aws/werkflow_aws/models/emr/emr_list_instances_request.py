from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EMRListInstancesRequest(BaseModel):
    ClusterId: StrictStr
    InstanceGroupId: StrictStr | None = None
    InstanceGroupTypes: list[Literal['MASTER', 'CORE', 'TASK']] | None = None
    InstanceFleetId: StrictStr | None = None
    InstanceFleetType: Literal['MASTER', 'CORE', 'TASK'] | None = None
    InstanceStates: list[Literal['AWAITING_FULFILLMENT', 'PROVISIONING', 'BOOTSTRAPPING', 'RUNNING', 'TERMINATED']] | None = None
    Marker: StrictStr | None = None
