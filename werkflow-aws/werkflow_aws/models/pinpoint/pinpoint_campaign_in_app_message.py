from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_in_app_message_content import PinpointInAppMessageContent


class PinpointCampaignInAppMessage(BaseModel):
    Body: StrictStr | None = None
    Content: list[PinpointInAppMessageContent] | None = None
    CustomConfig: dict[StrictStr, StrictStr] | None = None
    Layout: StrictStr | None = None
