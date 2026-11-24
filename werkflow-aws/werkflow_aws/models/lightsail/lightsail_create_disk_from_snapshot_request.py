from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .lightsail_add_on_request import LightsailAddOnRequest
from .lightsail_tag import LightsailTag


class LightsailCreateDiskFromSnapshotRequest(BaseModel):
    diskName: StrictStr
    availabilityZone: StrictStr
    sizeInGb: StrictInt
    diskSnapshotName: StrictStr | None = None
    tags: list[LightsailTag] | None = None
    addOns: list[LightsailAddOnRequest] | None = None
    sourceDiskName: StrictStr | None = None
    restoreDate: StrictStr | None = None
    useLatestRestorableAutoSnapshot: StrictBool | None = None
