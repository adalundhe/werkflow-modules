from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_routing_criteria_input import ConnectRoutingCriteriaInput


class ConnectUpdateContactRoutingDataRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    QueueTimeAdjustmentSeconds: StrictInt | None = None
    QueuePriority: StrictInt | None = None
    RoutingCriteria: ConnectRoutingCriteriaInput | None = None
