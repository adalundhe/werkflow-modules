from __future__ import annotations
from pydantic import BaseModel
from .pinpoint_in_app_message_campaign import PinpointInAppMessageCampaign


class PinpointInAppMessagesResponse(BaseModel):
    InAppMessageCampaigns: list[PinpointInAppMessageCampaign] | None = None
