from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_in_app_message_body_config import PinpointInAppMessageBodyConfig
from .pinpoint_in_app_message_button import PinpointInAppMessageButton
from .pinpoint_in_app_message_header_config import PinpointInAppMessageHeaderConfig


class PinpointInAppMessageContent(BaseModel):
    BackgroundColor: StrictStr | None = None
    BodyConfig: PinpointInAppMessageBodyConfig | None = None
    HeaderConfig: PinpointInAppMessageHeaderConfig | None = None
    ImageUrl: StrictStr | None = None
    PrimaryBtn: PinpointInAppMessageButton | None = None
    SecondaryBtn: PinpointInAppMessageButton | None = None
