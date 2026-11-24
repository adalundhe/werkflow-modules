from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .lightsail_destination_info import LightsailDestinationInfo
from .lightsail_export_snapshot_record_source_info import LightsailExportSnapshotRecordSourceInfo
from .lightsail_resource_location import LightsailResourceLocation


class LightsailExportSnapshotRecord(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    location: LightsailResourceLocation | None = None
    resourceType: StrictStr | None = None
    state: StrictStr | None = None
    sourceInfo: LightsailExportSnapshotRecordSourceInfo | None = None
    destinationInfo: LightsailDestinationInfo | None = None
