from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetCampaignVersionsRequest(BaseModel):
    ApplicationId: StrictStr
    CampaignId: StrictStr
    PageSize: StrictStr | None = None
    Token: StrictStr | None = None
