from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .personalize_campaign_config import PersonalizeCampaignConfig


class PersonalizeUpdateCampaignRequest(BaseModel):
    campaignArn: StrictStr
    solutionVersionArn: StrictStr | None = None
    minProvisionedTPS: StrictInt | None = None
    campaignConfig: PersonalizeCampaignConfig | None = None
