from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceRecordingModeOverride(BaseModel):
    description: StrictStr | None = None
    resourceTypes: list[StrictStr] | None = None
    recordingFrequency: StrictStr | None = None
