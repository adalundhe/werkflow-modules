from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_approximate_drifted_resource_count import ConnectApproximateDriftedResourceCount
from .connect_replication_finding import ConnectReplicationFinding
from .connect_resource_replication_status import ConnectResourceReplicationStatus


class ConnectListReplicationFindingsResponse(BaseModel):
    ReplicationFindingsList: list[ConnectReplicationFinding] | None = None
    ApproximateDriftedResourceCounts: list[ConnectApproximateDriftedResourceCount] | None = None
    NextToken: StrictStr | None = None
    ResourceReplicationStatuses: list[ConnectResourceReplicationStatus] | None = None
    ResponseMetadata: dict[str, Any] | None = None
