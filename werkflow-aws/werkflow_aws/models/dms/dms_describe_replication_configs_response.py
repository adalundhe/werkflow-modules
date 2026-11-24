from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_replication_config import DMSReplicationConfig


class DMSDescribeReplicationConfigsResponse(BaseModel):
    Marker: StrictStr | None = None
    ReplicationConfigs: list[DMSReplicationConfig] | None = None
    ResponseMetadata: dict[str, Any] | None = None
