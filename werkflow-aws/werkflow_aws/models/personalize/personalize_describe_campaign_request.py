from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDescribeCampaignRequest(BaseModel):
    campaignArn: StrictStr
