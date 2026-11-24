from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .connect_routing_profile_queue_reference import ConnectRoutingProfileQueueReference


class ConnectRoutingProfileQueueConfig(BaseModel):
    QueueReference: ConnectRoutingProfileQueueReference
    Priority: StrictInt
    Delay: StrictInt
