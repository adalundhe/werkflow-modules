from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetCampaignRequest(BaseModel):
    ApplicationId: StrictStr
    CampaignId: StrictStr
