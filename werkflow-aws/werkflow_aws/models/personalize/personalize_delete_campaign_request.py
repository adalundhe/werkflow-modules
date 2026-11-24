from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDeleteCampaignRequest(BaseModel):
    campaignArn: StrictStr
