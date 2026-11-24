from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESGetDomainDeliverabilityCampaignRequest(BaseModel):
    CampaignId: StrictStr
