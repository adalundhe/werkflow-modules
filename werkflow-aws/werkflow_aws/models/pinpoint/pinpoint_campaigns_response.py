from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_campaign_response import PinpointCampaignResponse


class PinpointCampaignsResponse(BaseModel):
    Item: list[PinpointCampaignResponse] | None = None
    NextToken: StrictStr | None = None
