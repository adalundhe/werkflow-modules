from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .personalize_campaign_config import PersonalizeCampaignConfig
from .personalize_tag import PersonalizeTag


class PersonalizeCreateCampaignRequest(BaseModel):
    name: StrictStr
    solutionVersionArn: StrictStr
    minProvisionedTPS: StrictInt | None = None
    campaignConfig: PersonalizeCampaignConfig | None = None
    tags: list[PersonalizeTag] | None = None
