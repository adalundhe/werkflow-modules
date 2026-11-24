from __future__ import annotations
from pydantic import BaseModel
from .rekognition_connected_home_settings_for_update import RekognitionConnectedHomeSettingsForUpdate


class RekognitionStreamProcessorSettingsForUpdate(BaseModel):
    ConnectedHomeForUpdate: RekognitionConnectedHomeSettingsForUpdate | None = None
