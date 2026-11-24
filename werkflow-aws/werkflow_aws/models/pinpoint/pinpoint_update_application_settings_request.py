from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_write_application_settings_request import PinpointWriteApplicationSettingsRequest


class PinpointUpdateApplicationSettingsRequest(BaseModel):
    ApplicationId: StrictStr
    WriteApplicationSettingsRequest: PinpointWriteApplicationSettingsRequest
