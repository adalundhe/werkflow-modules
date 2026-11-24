from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_replication import DMSReplication


class DMSDescribeReplicationsResponse(BaseModel):
    Marker: StrictStr | None = None
    Replications: list[DMSReplication] | None = None
    ResponseMetadata: dict[str, Any] | None = None
