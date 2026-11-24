from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_cloud_formation_stack_record import LightsailCloudFormationStackRecord


class LightsailGetCloudFormationStackRecordsResponse(BaseModel):
    cloudFormationStackRecords: list[LightsailCloudFormationStackRecord] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
