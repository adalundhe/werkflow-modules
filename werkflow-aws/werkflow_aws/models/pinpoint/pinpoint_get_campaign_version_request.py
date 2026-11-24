from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetCampaignVersionRequest(BaseModel):
    ApplicationId: StrictStr
    CampaignId: StrictStr
    Version: StrictStr
