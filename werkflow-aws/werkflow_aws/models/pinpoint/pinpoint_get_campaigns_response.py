from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_campaigns_response import PinpointCampaignsResponse


class PinpointGetCampaignsResponse(BaseModel):
    CampaignsResponse: PinpointCampaignsResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
