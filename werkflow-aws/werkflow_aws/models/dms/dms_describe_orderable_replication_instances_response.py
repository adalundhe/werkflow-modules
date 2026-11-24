from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_orderable_replication_instance import DMSOrderableReplicationInstance


class DMSDescribeOrderableReplicationInstancesResponse(BaseModel):
    OrderableReplicationInstances: list[DMSOrderableReplicationInstance] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
