from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_routing_profile_manual_assignment_queue_config_summary import ConnectRoutingProfileManualAssignmentQueueConfigSummary


class ConnectListRoutingProfileManualAssignmentQueuesResponse(BaseModel):
    NextToken: StrictStr | None = None
    RoutingProfileManualAssignmentQueueConfigSummaryList: list[ConnectRoutingProfileManualAssignmentQueueConfigSummary] | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
