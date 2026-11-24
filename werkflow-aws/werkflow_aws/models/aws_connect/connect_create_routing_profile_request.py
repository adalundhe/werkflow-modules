from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .connect_media_concurrency import ConnectMediaConcurrency
from .connect_routing_profile_manual_assignment_queue_config import ConnectRoutingProfileManualAssignmentQueueConfig
from .connect_routing_profile_queue_config import ConnectRoutingProfileQueueConfig


class ConnectCreateRoutingProfileRequest(BaseModel):
    InstanceId: StrictStr
    Name: StrictStr
    Description: StrictStr
    DefaultOutboundQueueId: StrictStr
    MediaConcurrencies: list[ConnectMediaConcurrency]
    QueueConfigs: list[ConnectRoutingProfileQueueConfig] | None = None
    ManualAssignmentQueueConfigs: list[ConnectRoutingProfileManualAssignmentQueueConfig] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    AgentAvailabilityTimer: Literal['TIME_SINCE_LAST_ACTIVITY', 'TIME_SINCE_LAST_INBOUND'] | None = None
