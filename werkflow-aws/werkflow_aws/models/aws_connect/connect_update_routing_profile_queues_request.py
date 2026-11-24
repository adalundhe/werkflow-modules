from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_routing_profile_queue_config import ConnectRoutingProfileQueueConfig


class ConnectUpdateRoutingProfileQueuesRequest(BaseModel):
    InstanceId: StrictStr
    RoutingProfileId: StrictStr
    QueueConfigs: list[ConnectRoutingProfileQueueConfig]
