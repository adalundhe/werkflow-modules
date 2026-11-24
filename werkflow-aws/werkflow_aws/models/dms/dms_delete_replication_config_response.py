from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dms_replication_config import DMSReplicationConfig


class DMSDeleteReplicationConfigResponse(BaseModel):
    ReplicationConfig: DMSReplicationConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
