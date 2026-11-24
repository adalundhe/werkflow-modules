from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .lightsail_add_on_request import LightsailAddOnRequest
from .lightsail_disk_map import LightsailDiskMap
from .lightsail_tag import LightsailTag


class LightsailCreateInstancesFromSnapshotRequest(BaseModel):
    instanceNames: list[StrictStr]
    availabilityZone: StrictStr
    bundleId: StrictStr
    attachedDiskMapping: dict[StrictStr, list[LightsailDiskMap]] | None = None
    instanceSnapshotName: StrictStr | None = None
    userData: StrictStr | None = None
    keyPairName: StrictStr | None = None
    tags: list[LightsailTag] | None = None
    addOns: list[LightsailAddOnRequest] | None = None
    ipAddressType: Literal['dualstack', 'ipv4', 'ipv6'] | None = None
    sourceInstanceName: StrictStr | None = None
    restoreDate: StrictStr | None = None
    useLatestRestorableAutoSnapshot: StrictBool | None = None
