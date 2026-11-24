from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt


class SSMDescribePatchGroupStateResponse(BaseModel):
    Instances: StrictInt | None = None
    InstancesWithInstalledPatches: StrictInt | None = None
    InstancesWithInstalledOtherPatches: StrictInt | None = None
    InstancesWithInstalledPendingRebootPatches: StrictInt | None = None
    InstancesWithInstalledRejectedPatches: StrictInt | None = None
    InstancesWithMissingPatches: StrictInt | None = None
    InstancesWithFailedPatches: StrictInt | None = None
    InstancesWithNotApplicablePatches: StrictInt | None = None
    InstancesWithUnreportedNotApplicablePatches: StrictInt | None = None
    InstancesWithCriticalNonCompliantPatches: StrictInt | None = None
    InstancesWithSecurityNonCompliantPatches: StrictInt | None = None
    InstancesWithOtherNonCompliantPatches: StrictInt | None = None
    InstancesWithAvailableSecurityUpdates: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
