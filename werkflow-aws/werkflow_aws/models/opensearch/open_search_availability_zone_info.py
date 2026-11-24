from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchAvailabilityZoneInfo(BaseModel):
    AvailabilityZoneName: StrictStr | None = None
    ZoneStatus: StrictStr | None = None
    ConfiguredDataNodeCount: StrictStr | None = None
    AvailableDataNodeCount: StrictStr | None = None
    TotalShards: StrictStr | None = None
    TotalUnAssignedShards: StrictStr | None = None
