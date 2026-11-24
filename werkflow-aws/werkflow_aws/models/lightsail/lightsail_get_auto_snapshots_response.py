from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_auto_snapshot_details import LightsailAutoSnapshotDetails


class LightsailGetAutoSnapshotsResponse(BaseModel):
    resourceName: StrictStr | None = None
    resourceType: StrictStr | None = None
    autoSnapshots: list[LightsailAutoSnapshotDetails] | None = None
    ResponseMetadata: dict[str, Any] | None = None
