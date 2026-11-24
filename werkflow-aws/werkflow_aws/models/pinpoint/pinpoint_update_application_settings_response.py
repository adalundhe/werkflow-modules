from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_application_settings_resource import PinpointApplicationSettingsResource


class PinpointUpdateApplicationSettingsResponse(BaseModel):
    ApplicationSettingsResource: PinpointApplicationSettingsResource | None = None
    ResponseMetadata: dict[str, Any] | None = None
