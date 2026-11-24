from __future__ import annotations
from pydantic import BaseModel
from .pinpoint_default_button_configuration import PinpointDefaultButtonConfiguration
from .pinpoint_override_button_configuration import PinpointOverrideButtonConfiguration


class PinpointInAppMessageButton(BaseModel):
    Android: PinpointOverrideButtonConfiguration | None = None
    DefaultConfig: PinpointDefaultButtonConfiguration | None = None
    IOS: PinpointOverrideButtonConfiguration | None = None
    Web: PinpointOverrideButtonConfiguration | None = None
