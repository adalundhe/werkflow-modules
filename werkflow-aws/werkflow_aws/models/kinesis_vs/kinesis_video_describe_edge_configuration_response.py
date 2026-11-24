from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .kinesis_video_edge_agent_status import KinesisVideoEdgeAgentStatus
from .kinesis_video_edge_config import KinesisVideoEdgeConfig


class KinesisVideoDescribeEdgeConfigurationResponse(BaseModel):
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    SyncStatus: StrictStr | None = None
    FailedStatusDetails: StrictStr | None = None
    EdgeConfig: KinesisVideoEdgeConfig | None = None
    EdgeAgentStatus: KinesisVideoEdgeAgentStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
