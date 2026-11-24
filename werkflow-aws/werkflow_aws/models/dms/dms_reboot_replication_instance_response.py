from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dms_replication_instance import DMSReplicationInstance


class DMSRebootReplicationInstanceResponse(BaseModel):
    ReplicationInstance: DMSReplicationInstance | None = None
    ResponseMetadata: dict[str, Any] | None = None
