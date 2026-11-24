from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .pinpoint_in_app_message_content import PinpointInAppMessageContent


class PinpointInAppTemplateRequest(BaseModel):
    Content: list[PinpointInAppMessageContent] | None = None
    CustomConfig: dict[StrictStr, StrictStr] | None = None
    Layout: Literal['BOTTOM_BANNER', 'TOP_BANNER', 'OVERLAYS', 'MOBILE_FEED', 'MIDDLE_BANNER', 'CAROUSEL'] | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    TemplateDescription: StrictStr | None = None
