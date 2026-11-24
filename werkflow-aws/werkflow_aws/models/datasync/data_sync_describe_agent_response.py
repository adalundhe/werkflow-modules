from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_sync_platform import DataSyncPlatform
from .data_sync_private_link_config import DataSyncPrivateLinkConfig


class DataSyncDescribeAgentResponse(BaseModel):
    AgentArn: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    LastConnectionTime: datetime.datetime | StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    EndpointType: StrictStr | None = None
    PrivateLinkConfig: DataSyncPrivateLinkConfig | None = None
    Platform: DataSyncPlatform | None = None
    ResponseMetadata: dict[str, Any] | None = None
