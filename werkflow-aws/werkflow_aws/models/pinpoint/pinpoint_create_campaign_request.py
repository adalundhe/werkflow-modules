from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_write_campaign_request import PinpointWriteCampaignRequest


class PinpointCreateCampaignRequest(BaseModel):
    ApplicationId: StrictStr
    WriteCampaignRequest: PinpointWriteCampaignRequest
