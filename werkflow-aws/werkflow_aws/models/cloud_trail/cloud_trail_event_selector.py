from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_trail_data_resource import CloudTrailDataResource


class CloudTrailEventSelector(BaseModel):
    ReadWriteType: StrictStr | None = None
    IncludeManagementEvents: StrictBool | None = None
    DataResources: list[CloudTrailDataResource] | None = None
    ExcludeManagementEventSources: list[StrictStr] | None = None
