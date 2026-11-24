from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .config_service_exclusion_by_resource_types import ConfigServiceExclusionByResourceTypes
from .config_service_recording_strategy import ConfigServiceRecordingStrategy


class ConfigServiceRecordingGroup(BaseModel):
    allSupported: StrictBool | None = None
    includeGlobalResourceTypes: StrictBool | None = None
    resourceTypes: list[StrictStr] | None = None
    exclusionByResourceTypes: ConfigServiceExclusionByResourceTypes | None = None
    recordingStrategy: ConfigServiceRecordingStrategy | None = None
