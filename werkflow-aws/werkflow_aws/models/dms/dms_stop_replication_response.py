from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dms_replication import DMSReplication


class DMSStopReplicationResponse(BaseModel):
    Replication: DMSReplication | None = None
    ResponseMetadata: dict[str, Any] | None = None
