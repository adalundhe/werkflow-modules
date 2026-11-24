from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .lightsail_disk_snapshot_info import LightsailDiskSnapshotInfo
from .lightsail_instance_snapshot_info import LightsailInstanceSnapshotInfo


class LightsailExportSnapshotRecordSourceInfo(BaseModel):
    resourceType: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    name: StrictStr | None = None
    arn: StrictStr | None = None
    fromResourceName: StrictStr | None = None
    fromResourceArn: StrictStr | None = None
    instanceSnapshotInfo: LightsailInstanceSnapshotInfo | None = None
    diskSnapshotInfo: LightsailDiskSnapshotInfo | None = None
