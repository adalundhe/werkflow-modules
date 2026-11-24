from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_campaign_response import PinpointCampaignResponse


class PinpointUpdateCampaignResponse(BaseModel):
    CampaignResponse: PinpointCampaignResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
