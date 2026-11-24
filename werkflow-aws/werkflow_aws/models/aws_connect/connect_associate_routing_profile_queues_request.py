from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_routing_profile_manual_assignment_queue_config import ConnectRoutingProfileManualAssignmentQueueConfig
from .connect_routing_profile_queue_config import ConnectRoutingProfileQueueConfig


class ConnectAssociateRoutingProfileQueuesRequest(BaseModel):
    InstanceId: StrictStr
    RoutingProfileId: StrictStr
    QueueConfigs: list[ConnectRoutingProfileQueueConfig] | None = None
    ManualAssignmentQueueConfigs: list[ConnectRoutingProfileManualAssignmentQueueConfig] | None = None
