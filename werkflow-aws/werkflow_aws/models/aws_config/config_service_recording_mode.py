from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_recording_mode_override import ConfigServiceRecordingModeOverride


class ConfigServiceRecordingMode(BaseModel):
    recordingFrequency: StrictStr | None = None
    recordingModeOverrides: list[ConfigServiceRecordingModeOverride] | None = None
