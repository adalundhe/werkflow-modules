from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .open_search_environment_info import OpenSearchEnvironmentInfo


class OpenSearchDescribeDomainHealthResponse(BaseModel):
    DomainState: StrictStr | None = None
    AvailabilityZoneCount: StrictStr | None = None
    ActiveAvailabilityZoneCount: StrictStr | None = None
    StandByAvailabilityZoneCount: StrictStr | None = None
    DataNodeCount: StrictStr | None = None
    DedicatedMaster: StrictBool | None = None
    MasterEligibleNodeCount: StrictStr | None = None
    WarmNodeCount: StrictStr | None = None
    MasterNode: StrictStr | None = None
    ClusterHealth: StrictStr | None = None
    TotalShards: StrictStr | None = None
    TotalUnAssignedShards: StrictStr | None = None
    EnvironmentInformation: list[OpenSearchEnvironmentInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
