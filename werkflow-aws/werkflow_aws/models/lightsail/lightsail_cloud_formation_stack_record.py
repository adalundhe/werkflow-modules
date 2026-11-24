from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .lightsail_cloud_formation_stack_record_source_info import LightsailCloudFormationStackRecordSourceInfo
from .lightsail_destination_info import LightsailDestinationInfo
from .lightsail_resource_location import LightsailResourceLocation


class LightsailCloudFormationStackRecord(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    location: LightsailResourceLocation | None = None
    resourceType: StrictStr | None = None
    state: StrictStr | None = None
    sourceInfo: list[LightsailCloudFormationStackRecordSourceInfo] | None = None
    destinationInfo: LightsailDestinationInfo | None = None
