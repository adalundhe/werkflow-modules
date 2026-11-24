from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointDeleteCampaignRequest(BaseModel):
    ApplicationId: StrictStr
    CampaignId: StrictStr
