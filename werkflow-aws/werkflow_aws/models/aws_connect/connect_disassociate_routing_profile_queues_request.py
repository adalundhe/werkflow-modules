from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_routing_profile_queue_reference import ConnectRoutingProfileQueueReference


class ConnectDisassociateRoutingProfileQueuesRequest(BaseModel):
    InstanceId: StrictStr
    RoutingProfileId: StrictStr
    QueueReferences: list[ConnectRoutingProfileQueueReference] | None = None
    ManualAssignmentQueueReferences: list[ConnectRoutingProfileQueueReference] | None = None
