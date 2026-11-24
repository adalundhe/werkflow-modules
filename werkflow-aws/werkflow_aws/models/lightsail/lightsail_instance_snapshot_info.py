from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_disk_info import LightsailDiskInfo


class LightsailInstanceSnapshotInfo(BaseModel):
    fromBundleId: StrictStr | None = None
    fromBlueprintId: StrictStr | None = None
    fromDiskInfo: list[LightsailDiskInfo] | None = None
