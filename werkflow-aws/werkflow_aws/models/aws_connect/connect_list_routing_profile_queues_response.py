from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_routing_profile_queue_config_summary import ConnectRoutingProfileQueueConfigSummary


class ConnectListRoutingProfileQueuesResponse(BaseModel):
    NextToken: StrictStr | None = None
    RoutingProfileQueueConfigSummaryList: list[ConnectRoutingProfileQueueConfigSummary] | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
