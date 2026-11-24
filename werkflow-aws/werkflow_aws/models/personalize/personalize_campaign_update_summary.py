from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .personalize_campaign_config import PersonalizeCampaignConfig


class PersonalizeCampaignUpdateSummary(BaseModel):
    solutionVersionArn: StrictStr | None = None
    minProvisionedTPS: StrictInt | None = None
    campaignConfig: PersonalizeCampaignConfig | None = None
    status: StrictStr | None = None
    failureReason: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
