from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .lightsail_tag import LightsailTag


class LightsailCreateRelationalDatabaseFromSnapshotRequest(BaseModel):
    relationalDatabaseName: StrictStr
    availabilityZone: StrictStr | None = None
    publiclyAccessible: StrictBool | None = None
    relationalDatabaseSnapshotName: StrictStr | None = None
    relationalDatabaseBundleId: StrictStr | None = None
    sourceRelationalDatabaseName: StrictStr | None = None
    restoreTime: datetime.datetime | StrictStr | None = None
    useLatestRestorableTime: StrictBool | None = None
    tags: list[LightsailTag] | None = None
